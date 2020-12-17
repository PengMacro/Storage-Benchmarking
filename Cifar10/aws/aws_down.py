import boto3
import os
from timeit import default_timer as timer
import cPickle as pickle

 
if __name__ == '__main__':


    s3 = boto3.client('s3', aws_access_key_id='AKIAJACOHPLSK5Z2Q7KA',
                      aws_secret_access_key='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')
    
    start = timer()
    data = {}
    
    i = 0
    while i < 50000: 
        filename = "img" + str(i)
        
        #s3.download_file('mnist-o', filename, '/home/cc/a/' + filename)

        data[filename] = s3.get_object(Bucket='cifar10-samples', Key=filename)['Body'].read()
        
        i += 1
        
    end = timer()
    print("download time: ", end - start) 
    
    start2 = timer()
    
    dict = {}


    for key, value in data.iteritems():
        dict[key] = pickle.loads(value)           
        
    end2 = timer()
    #print(dict)
    print("deserailze time: ", end2 - start2) 