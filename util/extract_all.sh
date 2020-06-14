#!/bin/bash

for d in ./*/ ; do
   gunzip $d/*.gz
done
#python3 hed.py --test --checkpoint ./data/hed_checkpoint.pt --output ~/Data/city_out_val --dataset ~/Data/CityScapes/img/val
