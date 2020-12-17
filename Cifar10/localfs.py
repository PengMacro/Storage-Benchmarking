import os
from timeit import default_timer as timer


#object_dir = "/home/cifar10_objects" #sda1(ext3)
#object_dir = "/home/ssd/cifar10_objects" #sda4(xfs)
object_dir = "/data/cifar10_objects" #sdb(ext4)


dict = {}
start = timer()

i = 0
while i < 50000: 
    filename = "img" + str(i)
    
    with open(os.path.join(object_dir, filename), 'rb') as file:
        dict.update({i: file.read()})
    
    i += 1
    
end = timer()
print("download time: ", end - start) 