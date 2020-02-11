import json, requests
from bs4 import BeautifulSoup
import pymysql

request_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
}

conn = pymysql.connect(host='localhost', user='root', password='##tkakrnl12', db='django_study', charset='utf8')
myCursor = conn.cursor()

main_url = 'http://www.ypbooks.co.kr/ypbooks/book/kor/getBookListMobileAjax.jsp'

for i in range(1, 11):
    print('-' * 50, '{}페이지 입니다.'.format(i))
    data = {
        'themeno': 'A000',
        'pageno': i,
        'method': 'getBestsellerScrollList',
    }
    req = requests.post(main_url, headers=request_headers, params=data)
    req_json = req.json()

    title = [req_json[x]['book_title'] for x in range(len(req_json))]
    price = [req_json[x]['salecost'] for x in range(len(req_json))]

    for c, v in zip(title, price):
        print(c, v)
        myCursor.execute(
            'INSERT INTO ypbooks('
            'title,'
            'price) VALUES("{}", "{}");'.format(
                title, price))

conn.commit()
conn.close()
