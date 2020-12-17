from cassandra.cluster import Cluster
import os
from cassandra.encoder import Encoder
import numpy as np
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



cluster = Cluster(['10.10.1.4'])
session = cluster.connect()

KEYSPACE = "cifar10"


session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
        """ % KEYSPACE)
 
session.set_keyspace(KEYSPACE)

session.execute("""
        CREATE TABLE IF NOT EXISTS blob (
            id int PRIMARY KEY,
            image blob,
            label int
        )
        """)



dir = './cifar-10-batches-py'

images, labels = load_cifar_10_data(dir)


pre = session.prepare("INSERT INTO blob (id, image, label) VALUES (?, ?, ?)");

i = 0
while i < 50000: 
    filename = "img" + str(i)
    
    bind = pre.bind((i, images[i], labels[i]));
    session.execute(bind);
    
    i += 1

