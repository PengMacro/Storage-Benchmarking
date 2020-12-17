#!/bin/bash


(ssh root@node0 sudo systemctl stop mongod; sync; echo 3 > /proc/sys/vm/drop_caches; sudo systemctl start mongod) &
# (ssh root@node1 sudo systemctl stop mongod; sync; echo 3 > /proc/sys/vm/drop_caches; sudo systemctl start mongod) &
# (ssh root@node2 sudo systemctl stop mongod; sync; echo 3 > /proc/sys/vm/drop_caches; sudo systemctl start mongod) &
# wait


python batch_down.py



