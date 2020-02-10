import json, requests, re
from bs4 import BeautifulSoup
import pymysql

main_url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'

request_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',

}

conn = pymysql.connect(host='localhost', user='root', password='##tkakrnl12', db='django_study', charset='utf8')
myCursor = conn.cursor()

max_page = 5


def tag_sub(tag):
    result = re.sub('<.+?>', '', tag, 0).strip()
    return result


def re_palce(tag):
    pattern = re.compile(r'\s+')
    sentence = re.sub(pattern, '', tag)
    return sentence


for page in range(1, max_page):
    data = {
        'orderClick': 'd79',
        'targetPage': page
    }
    print('-' * 50, page, '페이지 입니다.')
    req = requests.post(main_url, headers=request_headers, data=data)
    soup = BeautifulSoup(req.text, 'html.parser')
    for book in soup.select('div.detail'):
        title = str(book.select_one('div.title')).strip()
        author = str(book.select_one('div.author')).strip()
        price = str(book.select_one('strong.book_price')).strip()
        if title == 'None':
            print('제목이 없습니다.')
        else:
            title = tag_sub(title)
            author = tag_sub(author)
            author = re_palce(author)
            price = tag_sub(price)

            print(title, author, price)

            myCursor.execute(
                'INSERT INTO kyobos('
                'title,'
                'author,'
                'price) VALUES("{}", "{}", "{}");'.format(
                    title, author, price))
conn.commit()
conn.close()
