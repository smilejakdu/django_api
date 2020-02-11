import json, requests, re, pymysql
from bs4 import BeautifulSoup

main_url = 'http://www.yes24.com/24/category/bestseller'

request_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
}

conn = pymysql.connect(host='localhost', user='root', password='##tkakrnl12', db='django_study', charset='utf8')
myCursor = conn.cursor()


def re_palce(tag):
    pattern = re.compile(r'\s+')
    sentence = re.sub(pattern, '', tag)
    return sentence


for page in range(1, 11):
    print('-' * 50, '{}페이지 입니다.'.format(page))

    data = {
        'CategoryNumber': '001',
        'sumgb': '06',
        'fetchSize': '40',
        'PageNumber': page,
    }
    req = requests.get(main_url, headers=request_header, data=data)
    soup = BeautifulSoup(req.text, 'html.parser')
    for s in soup.select('td.goodsTxtInfo'):
        title = re_palce(s.select_one('p').text)
        price = re_palce(s.select_one('span.priceB').text)
        print(title, price)
        myCursor.execute(
            'INSERT INTO yess('
            'title,'
            'price) VALUES("{}", "{}");'.format(
                title, price))
conn.commit()
conn.close()
