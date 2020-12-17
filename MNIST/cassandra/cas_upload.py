# upload mnist objects to cassandra cluster
from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle

cluster = Cluster(['155.98.36.14'])

session = cluster.connect('test') # keyspace test has mnist1 table

object_dir = "./mnist_objects"

i = 0
while i < 60000: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
        
        ob = pickle.loads(file.read())        
        
        CQLString = "INSERT INTO mnist1 (id, image, label) VALUES (%s, %s, %s)"
        
        session.execute(CQLString, (i, ob['img'], ob['label']))
                
        i += 1


