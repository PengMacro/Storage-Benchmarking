from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import cPickle as pickle

cluster = Cluster(['10.10.1.4'])
session = cluster.connect('cifar10')



start = timer()
dict = {}

i = 0

rows = session.execute("SELECT * FROM blob")

for row in rows:
    dict.update({row.id: [row.image, row.label]})


end = timer()
#print(dict)
print(end - start)
