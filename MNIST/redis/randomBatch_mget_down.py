from rediscluster import RedisCluster
import os
import pickle
from timeit import default_timer as timer
import time
import math
import numpy as np

startup_nodes = [{"host": "10.10.1.1", "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

dataset_size = 60000
idx = [i for i in range(0, dataset_size)]
batch_size = 256
batch_num = int(math.ceil(dataset_size / batch_size))

data = {}
for epoch in range(1, 2):
    np.random.seed(9)
    np.random.shuffle(idx)
    print(idx[0:5])
    start = time.time()
    for i in range(0, batch_num):
        idx_batch = idx[batch_size * i:min(dataset_size, batch_size * (i + 1))]
        #print(mnist_collection.count_documents({}))
        # down_dict format {id, image, label}
        filename = ["img" + str(j) for j in idx_batch]
        dataList = rc.hmget("mnist", filename)
        #print(dataList[0])
    end = time.time()
    print(f"epoch time: {end - start}s")

'''
start2 = time.time()

for key, value in data.items():

    data[key] = pickle.loads(value.encode('utf-8'))
        
time.time()

end2 = timer()
print ("deserialize time: ", end2 - start2)  
'''