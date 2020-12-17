from rediscluster import RedisCluster
import os
import cPickle as pickle
from timeit import default_timer as timer

startup_nodes = [{"host": "10.10.1.1", "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

start = timer()

dictall = rc.hgetall("cifar10")

end = timer()
print ("download time: ", end - start)


start2 = timer()


dict = {}

for key, value in dictall.items():

    dict[key] = pickle.loads(value.encode('utf-8'))
        


end2 = timer()
print ("deserialize time: ", end2 - start2)  
