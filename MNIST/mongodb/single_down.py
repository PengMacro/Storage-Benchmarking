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


i = 0
while i < 60000: 
    
    down_dict = mnist_collection.find_one({"_id": i})
    data.append(down_dict)
    i += 1

    
end = timer()
print(end - start) 

#print(data) 
    


