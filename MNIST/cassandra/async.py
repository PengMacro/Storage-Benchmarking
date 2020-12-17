from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle

cluster = Cluster(['155.98.36.14'])

session = cluster.connect('test') # keyspace test has mnist table


start = timer()
dict = {}


i = 0
query = "SELECT * FROM mnist1 WHERE id = %s"



while i < 60000:
    
    future = session.execute_async(query, [i])

    rows = future.result()
    
    for row in rows:
        dict.update({row.id: [row.image, row.label]}) 
        
    
    i += 1
                

    
end = timer()
#print(dict)
print(end - start) 