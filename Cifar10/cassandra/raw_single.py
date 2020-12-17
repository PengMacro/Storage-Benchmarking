from cassandra.cluster import Cluster
import os
from timeit import default_timer as timer

cluster = Cluster(['10.10.1.4'])
session = cluster.connect('cifar10')

start = timer()
data = {}

pre = session.prepare("SELECT * FROM raw WHERE id = ?");

i = 0
while i < 50000: 
    
    bind = pre.bind([i]);
    rows = session.execute(bind);
    
    for row in rows:
        data.update({row.id: [row.image, row.label]}) 
        
    i += 1

end = timer()
print(end - start) 
