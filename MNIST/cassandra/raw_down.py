
# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from mnist import MNIST
from cassandra.encoder import Encoder

cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect('testkeyspace')

start = timer()
data = {}

pre = session.prepare("SELECT * FROM mnist_raw WHERE id = ?");

i = 0
while i < 60000: 
    
    bind = pre.bind([i]);
    rows = session.execute(bind);
    
    for row in rows:
        data.update({row.id: [row.image, row.label]}) 
        
    i += 1

end = timer()
print(end - start) 
