from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
app = Flask(__name__)

ca = certifi.where()

client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.gsiejtz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@ app.route('/')
def home():
    return render_template('index.html')


@ app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    doc = {'bucket': bucket_receive}
    db.bucketList.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})


@ app.route("/bucket", methods=["GET"])
def bucket_get():
    return list(db.bucketList.find({}, {'_id': False}))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
