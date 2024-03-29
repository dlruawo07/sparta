from pymongo import MongoClient
import requests, certifi
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

ca = certifi.where()

client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.gsiejtz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'title': ogtitle,
        'desc': ogdesc,
        'image': ogimage,
        'url': url_receive,
        'comment': comment_receive,
        'star': star_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


@app.route("/movie", methods=["GET"])
def movie_get():
    movies = list(db.movies.find({}, {'_id': False}))
    return movies


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
