#!/bin/bash

for d in ./*/ ; do
   gunzip $d/*.gz
done
