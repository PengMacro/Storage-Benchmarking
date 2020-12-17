import rados
import os
from timeit import default_timer as timer
import cPickle as pickle
import sys

#Create Handle Examples.
cluster = rados.Rados(conffile='./ceph.conf', conf = dict (keyring = './ceph.client.admin.keyring'))

cluster.connect()

print ("\nAvailable Pools")
pools = cluster.list_pools()

# only has rbd pool
for pool in pools:
    print (pool) 
    
     
ioctx = cluster.open_ioctx('rbd')


object_dir = './cifar10_objects'

i = 0
while i < 50000:
    filename = "img" + str(i)
    
    with open(os.path.join(object_dir, filename), 'rb') as file:
        
        ioctx.write_full(filename, file.read())
        
        #print(str(sys.getsizeof(file.read())))
        
        # file.seek(0)
        # print(file.read())
        
        i += 1

print ("\nClosing the connection.")
ioctx.close()


    
    