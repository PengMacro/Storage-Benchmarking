import pymongo
from pymongo import MongoClient
import pprint
import os
import numpy as np
import tarfile
import cPickle as pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


def load_cifar_10_data(dir):

    images = np.empty((5, 10000, 3072), dtype=np.uint8)
    labels = np.empty((5, 10000), dtype=np.uint8)

    for i in range(5):
        file_name = '{}/data_batch_{}'.format(dir, i + 1)
        d = unpickle(file_name)
        images[i] = d['data']
        labels[i] = d['labels']

    images = images.reshape(50000, 3072).tolist()
    labels = labels.reshape(50000).tolist()

    return images, labels


client = MongoClient('node3', 27017)

db = client.test_database
cifar10_collection = db.cifar10
cifar10_collection.remove({})


dir = './cifar-10-batches-py'

images, labels = load_cifar_10_data(dir)


i = 0
while i < 50000:     
    cifar10_collection.insert_one({"_id": i, "image": images[i], "labels": labels[i]}) # _id is the primary key
    i += 1

print(cifar10_collection.count_documents({}))

pprint.pprint(cifar10_collection.find_one())
