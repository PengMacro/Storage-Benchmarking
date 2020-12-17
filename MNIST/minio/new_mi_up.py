
from minio import Minio
#from minio.error import ResponseError
import os
import time
import math



if __name__ == '__main__':


    client = Minio('10.10.1.6:9000',
                      access_key='emulab_cmsc352_access',
                      secret_key='emulab_cmsc352_secret',
                      secure=False)
    
    granularity = 60000
    dataset_size = 60000
    object_dir = f"../mnist_objects_{granularity}"
    object_num = int(math.ceil(dataset_size / granularity))
    
    i = 0
    while i < object_num: 
        filename = "object" + str(i)
    
        with open(os.path.join(object_dir, filename), 'rb') as file:
            file_stat = os.stat(object_dir+"/"+filename)
            
            client.put_object(f"mnist-pickle-{granularity}", filename, file, file_stat.st_size)
            i += 1
