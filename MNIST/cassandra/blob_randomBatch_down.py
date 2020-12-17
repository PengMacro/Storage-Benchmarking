
# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from cassandra.encoder import Encoder
import math
import numpy as np
import time

cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect('testkeyspace')

start = timer()
data = {}

pre = session.prepare("SELECT * FROM mnist WHERE id = ?");

dataset_size = 60000
idx = [i for i in range(0, dataset_size)]
batch_size = 256
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
        for j in idx_batch:
            bind = pre.bind([i]);
            rows = session.execute(bind);
            for row in rows:
                data.update({row.id: [row.image, row.label]}) 
    end = time.time()
    print(f"epoch time: {end - start}s")

 