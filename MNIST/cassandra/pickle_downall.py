
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

rows = session.execute("SELECT * FROM mnist_dictstr") # pickle 

for row in rows:
    data.update({row.id: row.dict_data})

end = timer()
print("download time: ", end - start) 



start2 = timer()
dict = {}
for key, value in data.items():
    dict[key] = pickle.loads(value.encode('utf-8'))           
    
end2 = timer()
#print(dict)
print("deserailze time: ", end2 - start2) 