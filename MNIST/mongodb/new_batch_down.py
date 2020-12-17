import pymongo
from pymongo import MongoClient
import pprint
import time
import numpy as np
import math
import sys

client = MongoClient('node0', 27017)

db = client.test_database
mnist_collection = db.mnist


# 1, 2, 4, 16, 32, 64, 128, 256
batch_size = int(sys.argv[1])
#epochs = int(sys.argv[2])

dataset_size = 60000
idx = [i for i in range(0, dataset_size)]


batch_num = int(math.ceil(dataset_size / batch_size))

for epoch in range(1, 2):

    np.random.seed(9)
    np.random.shuffle(idx)
    #print(idx[0:5])
    data = []

    start = time.time()
    for i in range(0, batch_num):

        idx_batch = idx[batch_size * i:min(dataset_size, batch_size * (i + 1))]
        #print (idx_batch)

        for down_dict in mnist_collection.find({"_id": {"$in": idx_batch}}):
            data.append(down_dict)

    end = time.time()
    print("epoch time: ", (math.ceil((end - start)*100)/100))

#print(data)



