
from minio import Minio
from minio.error import ResponseError
import os
from timeit import default_timer as timer



if __name__ == '__main__':


    client = Minio('10.10.1.2:9000',
                      access_key='BKIKJAA5BMMU2RHO6IBB',
                      secret_key='V7f1CwQqAcwo80UEIJEjc5gVQUSSx5ohQ9GSrr12',
                      secure=False)
    
    
    object_dir = "./mnist_objects"
    
    i = 0
    while i < 60000: 
        filename = "img" + str(i)
    
        with open(os.path.join(object_dir, filename), 'rb') as file:
            file_stat = os.stat(object_dir+"/"+filename)
            
            client.put_object("mnist", filename, file, file_stat.st_size)
            i += 1
