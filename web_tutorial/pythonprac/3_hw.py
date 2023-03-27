from bs4 import BeautifulSoup  # 데이터를 가져오기 위한 라이브러리
import requests  # 웹에 접속하기 위한 라이브러리

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.melon.com/artistplus/artistchart/index.htm', headers=headers)

soup = BeautifulSoup(data.content, 'html.parser')

artists = []

lists = soup.select(
    '#conts > div.ltcont > div.wrap_list_artistplus.d_artist_list > ul > li')

for el in lists:
    image_url = el.select_one(
        'div.artistplus > div.wrap_thumb > a > img')['src']
    rank = el.select_one('div.artistplus_li_wrap > span.rank').text
    wrap_info = el.select_one('div.artistplus > div.wrap_info > dl')
    name = wrap_info.select_one('dt > a').text
    fan = wrap_info.select_one('dd.gubun').text[2:10].strip()
    # [0] : 음원 점수
    # [1] : 팬 증가수 점수
    # [2] : 좋아요 점수
    # [3] : 포토 점수
    # [4] : 비디오 점수
    # 점수들의 평균(이 때 음원 점수는 x4, 팬 증가수 점수는 x2)을 내어 순위를 정함
    score = list(map(float, wrap_info.select_one(
        'dd.consumer_list > table > tbody > tr').text.strip().split('\n')))
    score[0] *= 4
    score[1] *= 2
    average_point = str(round(sum(score) / len(score) / 1.8, 2))
    # print('image_url: '+image_url, 'rank: '+rank, 'name: ' +
    #       name, 'fan: '+fan, 'point: '+average_point, sep="\n")
    artists.append({
        "image_url": image_url,
        "rank": rank,
        "name": name,
        "fan": fan,
        "average_point": average_point
    })

for a in artists:
    print(a)
