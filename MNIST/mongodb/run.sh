#!/bin/bash


echo "test memory"


declare -a batch=("1" "2" "4" "16" "32" "64" "128" "256")
declare -a epochs=("1")


for i in "${batch[@]}"
do

   for j in "${epochs[@]}"
   do
    python3 peng.py $i $j

   done

done



for i in "${batch[@]}"
do

    ssh root@node0
    vmtouch -v /home/disk/mongodb/
    exit


   for j in "${epochs[@]}"
   do
    python3 peng.py $i $j

   done

done

