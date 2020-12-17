import boto3
import os

 
if __name__ == '__main__':


    object_dir = './mnist_objects'


    s3 = boto3.client('s3', aws_access_key_id='AKIAJJEM4UIFLCZ2GEDQ',
                      aws_secret_access_key='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')

    
    
    i = 0
    while i < 50000: 
        filename = "img" + str(i)
    
        with open(os.path.join(object_dir, filename), 'rb') as file:
            
            s3.put_object(Bucket="cifar", Key=filename, Body=file)
            
            i += 1