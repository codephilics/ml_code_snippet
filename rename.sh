#!/bin/bash

for i in *.jpg; do
  new=$(printf "shahrukh_%d.jpg" "$a") 
  mv -i -- "$i" "$new"
  let a=a+1
done
