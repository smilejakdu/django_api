import json, requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='##tkakrnl12', db='django_study', charset='utf8')
myCursor = conn.cursor()

main_url = 'https://www.aladin.co.kr/shop/common/wbest.aspx'

request_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
}

max_page = 10
for page in range(1, 10):
    print('-' * 50, '{}페이지 입니다.'.format(page))

    data = {
        'BestType': 'Bestseller',
        'BranchType': '1',
        'CID': '0',
        'page': page,
        'cnt': '1000',
        'SortOrder': '1',
    }

    req = requests.get(main_url, headers=request_header, data=data)
    soup = BeautifulSoup(req.text, 'html.parser')
    for s in soup.select('div.ss_book_box'):
        title = s.select_one('a.bo3').text
        price = s.select_one('span.ss_p2').text
        print(title, price)

        myCursor.execute(
            'INSERT INTO aladins('
            'title,'
            'price) VALUES("{}", "{}");'.format(
                title, price))

conn.commit()
conn.close()
