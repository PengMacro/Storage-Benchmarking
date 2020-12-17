
from minio import Minio
from minio.error import ResponseError

from timeit import default_timer as timer
import pickle


if __name__ == '__main__':


    client = Minio('10.10.1.2:9000',
                      access_key='BKIKJAA5BMMU2RHO6IBB',
                      secret_key='V7f1CwQqAcwo80UEIJEjc5gVQUSSx5ohQ9GSrr12',
                      secure=False)
    
    start = timer()  
    data = {}
    
    i = 0
    while i < 60000: 
        filename = "img" + str(i)
        data[filename] = client.get_object('mnist', filename).read()
        i += 1
    
    end = timer()
    print("download time: ", end - start) 
    
    
    
    dict = {}
    start2 = timer()
    for key, value in data.items():
        dict[key] = pickle.loads(value)        
    end2 = timer()
    print("items time: ", end2 - start2) 
