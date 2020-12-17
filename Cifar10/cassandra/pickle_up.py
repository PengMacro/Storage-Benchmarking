from cassandra.cluster import Cluster
import os
import numpy as np
import cPickle as pickle



cluster = Cluster(['10.10.1.4'])
session = cluster.connect()

KEYSPACE = "cifar10"

session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
        """ % KEYSPACE)
 
session.set_keyspace(KEYSPACE)

session.execute("""
        CREATE TABLE IF NOT EXISTS pickle_data (
            id int PRIMARY KEY,
            dict_data text
        )
        """)



object_dir = "./cifar10_objects"

pre = session.prepare("INSERT INTO pickle_data (id, dict_data) VALUES (?, ?)");

i = 0
while i < 50000: 
    
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
        
        #print(type(file.read())) # string
        
        bind = pre.bind((i, file.read()));
        session.execute(bind);
                        
        i += 1

