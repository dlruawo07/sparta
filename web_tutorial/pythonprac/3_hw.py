from bs4 import BeautifulSoup  # 데이터를 가져오기 위한 라이브러리
import requests  # 웹에 접속하기 위한 라이브러리

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.melon.com/artistplus/artistchart/index.htm', headers=headers)

soup = BeautifulSoup(data.content, 'html.parser')

artists = soup.select('#conts > div.ltcont > div.wrap_list_artistplus.d_artist_list > ul > li')

for artist in artists:
    rank = artist.select_one('div.artistplus_li_wrap > span.rank')
    name = artist.select_one('div.artistplus > div.wrap_info > dl > dt > a')
    print(rank.text, name.text)