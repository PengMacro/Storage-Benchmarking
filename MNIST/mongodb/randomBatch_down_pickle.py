import pymongo
from pymongo import MongoClient
import pprint
import time
import numpy as np
import math
import pickle

granularity = 4

client = MongoClient('node2', 27017)

db = client.test_database
mnist_collection = db[f'mnist_pickle_{granularity}']

dataset_size = round(60000 / granularity)
idx = [i for i in range(0, dataset_size)]
batch_size = 1
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
        # down_dict format {id, pickled object}
        for down_dict in mnist_collection.find({"_id": {"$in": idx_batch}}):
            data.append(down_dict)
    end = time.time()
    print(f"epoch time: {end - start}s")


'''
#print(data[0])
batch_example = data[0]['pickle_data']
print(pickle.loads(batch_example))
'''

start = time.time()
objects_unpickle = []
for down_dict in data:
    objects_unpickle.append(pickle.loads(down_dict['pickle_data']))
end = time.time()
print(f"deserialization time: {end - start}s")



