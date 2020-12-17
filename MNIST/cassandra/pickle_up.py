# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle
from mnist import MNIST
from cassandra.encoder import Encoder


cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect()

KEYSPACE = "testkeyspace"

session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)
 
session.set_keyspace(KEYSPACE)

session.execute("""
        CREATE TABLE IF NOT EXISTS mnist_dictstr (
            id int PRIMARY KEY,
            dict_data text
        )
        """)


object_dir = "./mnist_objects"

pre = session.prepare("INSERT INTO mnist_dictstr (id, dict_data) VALUES (?, ?)");

i = 0
while i < 60000: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
        
        #print(type(file.read())) # string
        
        bind = pre.bind((i, file.read()));
        session.execute(bind);
                        
        i += 1

