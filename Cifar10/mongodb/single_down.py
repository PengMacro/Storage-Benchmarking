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


i = 0
while i < 50000: 
    
    down_dict = cifar10_collection.find_one({"_id": i})
    data.append(down_dict)
    i += 1

    
end = timer()
print(end - start) 

#print(data) 
    


