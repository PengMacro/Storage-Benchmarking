from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer

cluster = Cluster(['10.10.1.4'])
session = cluster.connect('cifar10')


session.default_timeout = 6000

start = timer()
dict = {}

rows = session.execute("SELECT * FROM raw")

for row in rows:
    dict.update({row.id: [row.image, row.label]})

end = timer()
#print(dict)
print(end - start)
