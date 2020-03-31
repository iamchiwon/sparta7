from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.users.insert_one({'name': 'bobby', 'age': 21})

# print(db.users.find_one({'name': 'bobby'}))

db.users.update_many({'name': 'bobby'}, {'$unset': {'age2': 23}})

all_users = db.users.find()
for user in all_users:
    print(user)
