import boto3
import os
from timeit import default_timer as timer
import pickle


if __name__ == '__main__':


    s3 = boto3.client('s3', endpoint_url='http://s3.seagate.com')


    start = timer()
    data = {}

    i = 0
    while i < 60000:
        filename = "img" + str(i)

        data[filename] = s3.get_object(Bucket='mnist-samples', Key=filename)['Body'].read()

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