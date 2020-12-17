import rados
import os
from timeit import default_timer as timer
import cPickle as pickle
import sys

#Create Handle Examples.
cluster = rados.Rados(conffile='./ceph.conf', conf = dict (keyring = './ceph.client.admin.keyring'))

cluster.connect()


ioctx = cluster.open_ioctx('rbd')


start = timer()
data = {}

i = 0
while i < 50000:
        filename = "img" + str(i)
        
        data[filename] = ioctx.read(filename)
        #print(str(sys.getsizeof(data[filename])))
        
        i += 1
            
end = timer()
print("download time: ", end - start) 


dict = {}
start2 = timer()


# #data["img0"] = ioctx.read("img0")
# data["img1"] = ioctx.read("img9")

# print(type(data["img1"]))
# print(str(sys.getsizeof(data["img1"])))

# ioctx.close()

# #dict["img0"] = pickle.loads(data["img0"])  
# dict["img1"] = pickle.loads(data["img1"])  


ioctx.close()


for key, value in data.items():
    dict[key] = pickle.loads(value)  
    
end2 = timer()
print("deserailze time: ", end2 - start2) 
#print(dict.keys())

#ioctx.close()



    
    
