from rediscluster import RedisCluster
import os
import pickle
from timeit import default_timer as timer

startup_nodes = [{"host": "10.10.1.1", "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)


start = timer()
dict = {}

i = 0
while i < 60000: 
    filename = "img" + str(i)
        
    dict[filename] = rc.get(filename)
        
    i += 1


end = timer()
#print(dict)
print("download time: ", end - start) 


start2 = timer()

data = {}


for key, value in dict.items():
    data[key] = pickle.loads(value.encode('utf-8'))           
    
end2 = timer()
#print(dict)
print("deserailze time: ", end2 - start2) 