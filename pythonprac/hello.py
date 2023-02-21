import requests  # 웹에 접속하기 위한 라이브러리
from bs4 import BeautifulSoup  # 데이터를 가져오기 위한 라이브러리

from pymongo import MongoClient
import certifi

ca = certifi.where()

# mongoDB에서 connect -> connect your application -> driver: python 3.6 or later -> copy
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.gsiejtz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 웹에서 원하는 엘리먼트에 우클릭, 검사 -> copy -> copy selector
a = soup.select_one(
    '#old_content > table > tbody > tr:nth-child(3) > td.title > div > a')

# a에 담긴 <a href="/movie/bi/mi/basic.naver?code=171539" title="그린 북">그린 북</a> 중에 텍스트 부분만 가져오기
print(a.text)
# a에 담긴 <a href="/movie/bi/mi/basic.naver?code=171539" title="그린 북">그린 북</a> 중에 href 부분만 가져오기
print(a['href'])

# old_content > table > tbody > tr:nth-chid(2)
# old_content > table > tbody > tr:nth-chid(3)
trs = soup.select('#old_content > table > tbody > tr')  # tr들이 리스트로 저장됨

for tr in trs:
	# tr에서 <a href="/movie/bi/mi/basic.naver?code=OOOOOO" title="OOO">OOO</a> 가져오기
    title = tr.select_one('td.title > div > a')
    if title is not None:
        title = title.text
        #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        rank = tr.select_one('td').img['alt']
        #old_content > table > tbody > tr:nth-child(2) > td.point
        point = tr.select_one('td.point').text

        doc = {
            'title': title,
            'rank': rank,
            'point': point
        }

        db.movies.insert_one(doc) # movies라는 콜렉션에 doc 저장