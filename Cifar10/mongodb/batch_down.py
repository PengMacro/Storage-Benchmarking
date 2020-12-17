import pymongo
from pymongo import MongoClient
import pprint
from timeit import default_timer as timer

client = MongoClient('node3', 27017)

db = client.test_database
cifar10_collection = db.cifar10


data = []

start = timer()
#print(cifar10_collection.count_documents({}))

# down_dict format {id, image, label}
for down_dict in cifar10_collection.find():
    data.append(down_dict)

end = timer()
print(end - start) 

#print(data) 
    


