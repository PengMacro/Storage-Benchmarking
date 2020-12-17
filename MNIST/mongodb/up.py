import pymongo
from pymongo import MongoClient
import pprint
import os
import pickle
from mnist import MNIST

client = MongoClient('node2', 27017)

db = client.test_database
mnist_collection = db['mnist_raw']
mnist_collection.remove({})

#mnist_collection.createIndex( { "id": 1 }, { unique: true } )

raw = MNIST('./')
images, labels = raw.load_training()

i = 0
while i < 60000:     
    mnist_collection.insert_one({"_id": i, "image": images[i], "labels": labels[i]}) # _id is the primary key
    i += 1

print(mnist_collection.count_documents({}))

pprint.pprint(mnist_collection.find_one())






# mnist_dict = {}
# mnist_list = []


# i = 0
# while i < 2: 
#     filename = "img" + str(i)

#     with open(os.path.join(object_dir, filename), 'rb') as file:
        
#         mnist_dict[str(i)] = file.read() 
        
#         #mnist.insert_one(mnist_dict).inserted_ids
        
#         mnist_list.append(mnist_dict.copy())
        
#         i += 1

# result = mnist.insert_many(mnist_list)



#pprint.pprint(mnist.find_one())


# dict = {}

# for down_dict in mnist.find():
#     for key, value in down_dict.items():
#         print(type(key))
#         print(type(value))
        #dict[key] = pickle.loads(value.encode('utf-8'))
       

    
    

#pprint.pprint(dict)
#print("deserailze time: ", end2 - start2) 
























