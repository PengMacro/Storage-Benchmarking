from timeit import default_timer as timer
import swiftclient
import os

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


container = "cifar10"

object_dir = "./cifar10_objects"

i = 0
while i < 10: 
    filename = "img" + str(i)

    with open(os.path.join(object_dir, filename), 'rb') as file:
        conn.put_object(container, filename, contents=file)
        i += 1




