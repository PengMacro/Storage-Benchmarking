
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import numpy
import cPickle as pickle
from cassandra.encoder import Encoder



cluster = Cluster(['10.10.1.4'])
session = cluster.connect('cifar10')

start = timer()
data = {}

pre = session.prepare("SELECT * FROM pickle_data WHERE id = ?");

i = 0
while i < 50000: 
    
    bind = pre.bind([i]);
    rows = session.execute(bind);
    
    for row in rows:
        data.update({row.id: row.dict_data}) 
        
    i += 1

end = timer()
print("download time: ", end - start) 


start2 = timer()

dict = {}



for key, value in data.items():
    dict[key] = pickle.loads(value.encode('latin1'))
    
end2 = timer()
#print(dict)
print("deserailze time: ", end2 - start2) 