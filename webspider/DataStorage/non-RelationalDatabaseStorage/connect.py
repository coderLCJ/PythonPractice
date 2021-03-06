import pymongo

# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
# 等价于 client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 等价于 db = client['test']

# 指定集合
collection = db.students
# 等价于 collection = db['students']

