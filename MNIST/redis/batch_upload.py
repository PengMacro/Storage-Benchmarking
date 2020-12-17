from rediscluster import RedisCluster
import os
import pickle
from timeit import default_timer as timer

startup_nodes = [{"host": "10.10.1.1", "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)


object_dir = "./mnist_objects"

i = 0
while i < 60000: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
                
        rc.hset("mnist", filename, file.read()) # hash name()str, key(str), value(string)
        
        
        # dict = pickle.loads(rc.get(filename))
        # print(dict)
                       
        i += 1


