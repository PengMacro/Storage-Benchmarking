import rados
import os
from timeit import default_timer as timer
import pickle

#Create Handle Examples.
cluster = rados.Rados(conffile='./ceph.conf', conf = dict (keyring = './ceph.client.admin.keyring'))

cluster.connect()


ioctx = cluster.open_ioctx('rbd')


start = timer()
data = {}

i = 0
while i < 60000:
        filename = "img" + str(i)
        
        data[filename] = ioctx.read(filename)

        i += 1
            
end = timer()
print("download time: ", end - start) 


dict = {}
start2 = timer()

for key, value in data.items():
    dict[key] = pickle.loads(value)  
    
end2 = timer()
print("deserailze time: ", end2 - start2) 
#print(dict)

ioctx.close()



    
    
