import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
res = collection.find_one({'age': 21})
print(res)
