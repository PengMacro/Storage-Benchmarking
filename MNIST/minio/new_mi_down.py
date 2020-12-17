
from minio import Minio
#from minio.error import ResponseError

import time
import pickle
import math


if __name__ == '__main__':


    client = Minio('10.10.1.6:9000',
                      access_key='emulab_cmsc352_access',
                      secret_key='emulab_cmsc352_secret',
                      secure=False)
    
    start = time.time()  
    data = {}
    
    granularity = 60000
    dataset_size = 60000
    object_dir = f"../mnist_objects_{granularity}"
    object_num = int(math.ceil(dataset_size / granularity))

    i = 0
    while i < object_num: 
        filename = "object" + str(i)
        data[filename] = client.get_object(f'mnist-pickle-{granularity}', filename).read()
        i += 1
    
    end = time.time()
    print("download time: ", end - start)
    #print(pickle.loads(data['object0']))
    
    
    '''
    dict = {}
    start2 = time.time()
    for key, value in data.items():
        dict[key] = pickle.loads(value)        
    end2 = time.time()
    print("items time: ", end2 - start2) 
    '''