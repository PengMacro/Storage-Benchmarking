
# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from cassandra.encoder import Encoder
import math
import numpy as np
import time
from cassandra import query

cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect('testkeyspace')

start = timer()
data = {}

pre = session.prepare("SELECT * FROM mnist_dictstr WHERE id IN ?");

dataset_size = 60000
idx = [i for i in range(0, dataset_size)]
batch_size = 32
batch_num = int(math.ceil(dataset_size / batch_size))

for epoch in range(1, 2):
    np.random.seed(9)
    np.random.shuffle(idx)
    print(idx[0:5])
    start = time.time()
    for i in range(0, batch_num):
        idx_batch = idx[batch_size * i:min(dataset_size, batch_size * (i + 1))]
        #print(mnist_collection.count_documents({}))
        # down_dict format {id, image, label}
        bind = pre.bind(query.ValueSequence([idx_batch]))
        rows = session.execute(bind)
        for row in rows:
            #print(row)
            data.update({row.id: row.dict_data}) 
    end = time.time()
    print(f"epoch time: {end - start}s")

 

'''
start2 = time.time()

for key, value in data.items():
    data[key] = pickle.loads(value.encode('utf-8'))           
    
end2 = time.time()
#print(dict)
print("deserailze time: ", end2 - start2)
'''