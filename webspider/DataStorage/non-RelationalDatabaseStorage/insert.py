import pymongo

student1 = {
    'id': '2704170205',
    'name': 'laity',
    'age': 21,
    'gender': 'male'
}

student2 = {
    'id': '2704170203',
    'name': 'laity2',
    'age': 21,
    'gender': 'female'
}

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
result = collection.insert_many([student1, student2])
print(result)
