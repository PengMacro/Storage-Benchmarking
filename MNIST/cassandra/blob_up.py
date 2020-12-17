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
        CREATE TABLE IF NOT EXISTS mnist (
            id int PRIMARY KEY,
            image blob,
            label int
        )
        """)


object_dir = "./mnist_objects"
raw = MNIST('./')
images, labels = raw.load_training()

#print(type(images[0]))

    

pre = session.prepare("INSERT INTO mnist (id, image, label) VALUES (?, ?, ?)");

i = 0
while i < 60000: 
    filename = "img" + str(i)
    
    bind = pre.bind((i, images[i], labels[i]));
    session.execute(bind);
    
    i += 1



# encoder = Encoder()
# i = 0
# while i < 1: 
#     filename = "img" + str(i)
#     #text = ' '.join(str(e) for e in images[i])
    
#     blob = encoder.cql_encode_bytes(str(images[i])) 
#     #blob = "textAsBlob('" + str(images[i]) + "')"
    
#     CQLString = "INSERT INTO mnist (id, image, label) VALUES (%s, ?, %s)"
    
#     session.execute(CQLString, (i, blob, images[i]))
    
#     i += 1






















# i = 0
# while i < 1: 
#     filename = "img" + str(i)

#     with open(os.path.join(object_dir, filename), 'rb') as file:
        
#         ob = pickle.loads(file.read())        
        
#         CQLString = "INSERT INTO mnist1 (id, image, label) VALUES (%s, %s, %s)"
        
#         session.execute(CQLString, (i, ob['img'], ob['label']))
                
#         i += 1

# i = 0
# while i < 60000: 
#     filename = "img" + str(i)
#     sample = {'img': images[i], 'label': labels[i]}

#     with open(os.path.join(object_dir, filename), 'wb') as file:
#         pickle.dump(sample, file)
#         i += 1