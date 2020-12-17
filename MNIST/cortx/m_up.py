import boto3
import os


if __name__ == '__main__':


    object_dir = './mnist_objects'

    # cortx
    s3 = boto3.client('s3', endpoint_url='https://s3.seagate.com')


    #print(s3.list_buckets())


    i = 0
    while i < 60000:
        filename = "img" + str(i)

        with open(os.path.join(object_dir, filename), 'rb') as file:

            s3.put_object(Bucket="mnist-samples", Key=filename, Body=file)

            i += 1
