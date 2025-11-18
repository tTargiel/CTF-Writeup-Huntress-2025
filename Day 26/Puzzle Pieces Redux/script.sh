#!/bin/bash

files=./*.bin

for f in $files
do
   echo "$f file"
   echo "--------"
   exiftool -PDBModifyDate -s $f
   strings -n8 $f | grep "flag_part"
   xxd $f | grep "000161c0"
   echo "--------"
done