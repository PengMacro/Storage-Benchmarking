from rediscluster import RedisCluster
import os
from timeit import default_timer as timer

startup_nodes = [{"host": "10.10.1.2", "port": "6379"}, ]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)


object_dir = "./cifar10_objects"

i = 0
while i < 50000: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
        
        
        rc.set(filename, file.read())
                       
        i += 1

