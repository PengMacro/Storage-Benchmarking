import rados
import os
from timeit import default_timer as timer
import pickle

#Create Handle Examples.
cluster = rados.Rados(conffile='./ceph.conf', conf = dict (keyring = './ceph.client.admin.keyring'))

cluster.connect()

print ("\nAvailable Pools")
pools = cluster.list_pools()

# only has rbd pool
for pool in pools:
    print (pool) 
     
     
ioctx = cluster.open_ioctx('rbd')


object_dir = './mnist_objects'


i = 0
while i < 60000:
    filename = "img" + str(i)
    
    with open(os.path.join(object_dir, filename), 'rb') as file:
            
        ioctx.write_full(filename, file.read())

        i += 1
            



print ("\nClosing the connection.")
ioctx.close()



    
    