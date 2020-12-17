import pymongo
from pymongo import MongoClient
import pprint
from timeit import default_timer as timer

client = MongoClient('node0', 27017)

db = client.test_database
mnist_collection = db.mnist


data = []

start = timer()
#print(mnist_collection.count_documents({}))

# down_dict format {id, image, label}
for down_dict in mnist_collection.find():
    data.append(down_dict)


end = timer()
print(end - start)

#print(data)



