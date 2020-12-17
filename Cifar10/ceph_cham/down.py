# run with python3
import os
from timeit import default_timer as timer
import swiftclient
import pickle

_authurl = 'https://chi.tacc.chameleoncloud.org:5000'
_auth_version = '3'
_user = 'pcpeng'
_key = 'xxxxx'
_os_options = {
    'user_domain_name': 'Default',
    'project_domain_name': 'Default',
    'project_name': 'CH-818141'
}

conn = swiftclient.Connection(
    authurl=_authurl,
    user=_user,
    key=_key,
    os_options=_os_options,
    auth_version=_auth_version
)


container_name = "cifar10"

start = timer()
data = {}

i = 0
while i < 50000: 
    filename = "img" + str(i)
    obj_tuple = conn.get_object(container_name, filename)
    data[filename] = obj_tuple[1]
    i += 1
    
end = timer()
print("download time: ", end - start) 

dict = {}
start2 = timer()
for key, value in data.items():
    dict[key] = pickle.loads(value)        
end2 = timer()
print("deser time: ", end2 - start2) 

