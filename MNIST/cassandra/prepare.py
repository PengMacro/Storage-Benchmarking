from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle

cluster = Cluster(['155.98.36.14'])

session = cluster.connect('test') # keyspace test has mnist table


start = timer()
dict = {}


i = 0
query = "SELECT * FROM mnist1 WHERE id = ?"

while i < 60000:
    
    pre = session.prepare(query);
    bind = pre.bind([i]);
    rows = session.execute(bind);
    
    
    for row in rows:
        dict.update({row.id: [row.image, row.label]}) 
        
    
    i += 1
                
    
end = timer()
#print(dict)
print(end - start) 