import pymongo

# �������ݿ�
client = pymongo.MongoClient(host='localhost', port=27017)
# �ȼ��� client = pymongo.MongoClient('mongodb://localhost:27017/')

# ָ�����ݿ�
db = client.test
# �ȼ��� db = client['test']

# ָ������
collection = db.students
# �ȼ��� collection = db['students']

