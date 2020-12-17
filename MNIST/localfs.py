import os
from timeit import default_timer as timer
import pickle


object_dir = "disk/mnist_objects"

dict = {}
start = timer()

i = 0
while i < 60000: 
    filename = "img" + str(i)
    
    with open(os.path.join(object_dir, filename), 'rb') as file:
        dict.update({i: file.read()})
    
    i += 1
    
end = timer()
print("download time: ", end - start) 