import pymongo
from pymongo import MongoClient
import pprint
import os
import numpy as np
import tarfile
import pickle




client = MongoClient('node2', 27017)

db = client.test_database2
cifar10_collection = db.cifar10_pickle
cifar10_collection.remove({})


object_dir = f'./cifar10_objects'



i = 0
while i < 50000:
    images_pickle = open(object_dir + f'/img{i}', 'rb')   
    cifar10_collection.insert_one({"_id": i, "pickle_data": images_pickle.read()}) # _id is the primary key
    i += 1

print(cifar10_collection.count_documents({}))

pprint.pprint(pickle.loads(cifar10_collection.find_one()['pickle_data']))
