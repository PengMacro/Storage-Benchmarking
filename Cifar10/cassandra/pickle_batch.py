from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import cPickle as pickle
from cassandra.encoder import Encoder

cluster = Cluster(['10.10.1.4'])
session = cluster.connect('cifar10')

start = timer()
data = {}

rows = session.execute("SELECT * FROM pickle_data") 

for row in rows:
    data.update({row.id: row.dict_data})

end = timer()
print("download time: ", end - start) 



start2 = timer()
dict = {}
for key, value in data.items():
    dict[key] = pickle.loads(value.encode('latin1'))           
    
end2 = timer()
#print(dict)
print("deserailze time: ", end2 - start2) 