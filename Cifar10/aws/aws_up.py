import boto3
import os


if __name__ == '__main__':


    object_dir = './cifar10_objects'


    s3 = boto3.client('s3', aws_access_key_id='xx',
                      aws_secret_access_key='xx')

    i = 0
    while i < 50000:
        filename = "img" + str(i)

        with open(os.path.join(object_dir, filename), 'rb') as file:

            s3.put_object(Bucket="cifar10-samples", Key=filename, Body=file)

            i += 1
