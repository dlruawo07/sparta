from pymongo import MongoClient
import certifi

ca = certifi.where()

# mongoDB에서 connect -> connect your application -> driver: python 3.6 or later -> copy
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.gsiejtz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name': '철수',
    'age': 24
}
db.users.insert_one(doc)
db.users.insert_one({'name': 'bobby', 'age': 21})

find = db.users.find({'name': '철수'})
print(list(find))

# 데이터마다 id값이 자동으로 생기는데 데이터 추출 시 누락시킬 수 있는 방법
# all_users = list(db.users.find({}, {'_id': False}))

# for user in all_users:
    # print(user)
