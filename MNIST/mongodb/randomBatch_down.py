import pymongo
from pymongo import MongoClient
import pprint
import time
import numpy as np
import math

client = MongoClient('node2', 27017)

db = client.test_database
mnist_collection = db.mnist

dataset_size = 60000
idx = [i for i in range(0, dataset_size)]
batch_size = 4
batch_num = int(math.ceil(dataset_size / batch_size))

for epoch in range(1, 2):
    np.random.seed(9)
    np.random.shuffle(idx)
    print(idx[0:5])
    data = []
    start = time.time()
    for i in range(0, batch_num):
        idx_batch = idx[batch_size * i:min(dataset_size, batch_size * (i + 1))]
        #print(mnist_collection.count_documents({}))
        # down_dict format {id, image, label}
        for j in idx_batch:
            down_dict = mnist_collection.find_one({"_id": j})
            data.append(down_dict)
    end = time.time()
    print(f"epoch time: {end - start}s") 

#print(data) 
    


