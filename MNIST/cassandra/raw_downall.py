from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer
import pickle

cluster = Cluster(['10.10.1.1', '10.10.1.1'])
session = cluster.connect('testkeyspace')

session.default_timeout = 6000

start = timer()
dict = {}

i = 0

rows = session.execute("SELECT * FROM mnist_raw")

for row in rows:
    dict.update({row.id: [row.image, row.label]})

end = timer()
#print(dict)
print(end - start)
