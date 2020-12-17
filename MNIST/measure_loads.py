import os
from timeit import default_timer as timer
import pickle


object_dir = "./mnist_objects"

start = timer()

i = 0
while i < 60000: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file: # open spend 5s
        
        ob = pickle.loads(file.read())         
                
        i += 1


end = timer()
print(end - start) 

