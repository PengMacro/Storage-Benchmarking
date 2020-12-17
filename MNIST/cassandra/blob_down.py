# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from mnist import MNIST

cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect('testkeyspace')

start = timer()
dict = {}

i = 0

pre = session.prepare("SELECT * FROM mnist WHERE id = ?");

while i < 60000:
    
    bind = pre.bind([i]);
    rows = session.execute(bind);
    
    for row in rows:
        dict.update({row.id: [row.image, row.label]}) 
        
    i += 1
                  
end = timer()
#print(dict)
print(end - start) 

