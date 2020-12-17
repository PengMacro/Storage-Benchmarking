# remote fetch using ceph
import logging
import os

from swiftclient.service import SwiftService, SwiftError
from timeit import default_timer as timer

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


#objects = ["object_MINST/img0"]


# with SwiftService(options=auth) as swift:
#     for down_res in swift.download(container=container,objects=objects, options=op):
        
#         if down_res['success']:
#             print("'%s' downloaded" % down_res['object'])
#         else:
#             print("'%s' download failed" % down_res['object'])
            
#         print(down_res['object'])



# op ={'out_directory': "./download", }

#op ={'out_directory': "./test", 'out_file': "./a", 'no_download': True}

# 'no_download': False, no data is written back to disk, default


# op ={'out_directory': "./test", 'no_download': False, 'object_dd_threads': 50}


# start = timer()

# with SwiftService(options=auth) as swift:
#     try:        
#         list_parts_gen = swift.list(container=container)
#         for page in list_parts_gen:
#             if page["success"]:
                
#                 objects = [obj["name"] for obj in page["listing"]]
#                 swift.download(container=container,objects=objects,options=op)
               
                
#             else:
#                 raise page["error"]
#     except SwiftError as e:
#         logger.error(e.value)

# end = timer()
# print(end - start) 



op = {
    "out_directory": "./a",
    "no_download": True,      # write to disk if false, if true, not download
    "object_dd_threads": 10
}

container = "MNIST-o"

#container = "aaaa"

start = timer()

with SwiftService(options=op) as swift:
    try:        
        
        for a in swift.download(container=container):
            #print (a)
            pass
               
                
    except SwiftError as e:
        logger.error(e.value)

end = timer()
print(end - start) 