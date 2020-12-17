# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from mnist import MNIST
from cassandra.encoder import Encoder


cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect()

KEYSPACE = "testkeyspace_raw"

session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)
 
session.set_keyspace(KEYSPACE)

session.execute("""
        CREATE TABLE IF NOT EXISTS mnist_raw (
            id int PRIMARY KEY,
            image list<int>,
            label int 
        )
        """)


object_dir = "./mnist_objects"
raw = MNIST('./')
images, labels = raw.load_training()

pre = session.prepare("INSERT INTO mnist_raw (id, image, label) VALUES (?, ?, ?)");

i = 0
while i < 60000: 
    filename = "img" + str(i)        
        
    bind = pre.bind((i, images[i], labels[i]));
    session.execute(bind);
                    
    i += 1

