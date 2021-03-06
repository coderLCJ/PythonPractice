import pymongo


student = {
    'id': '2704170205',
    'name': 'laity',
    'age': 21,
    'gender': 'male'
}

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
result = collection.insert(student)
print(result)