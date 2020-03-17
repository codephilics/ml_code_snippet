#!/bin/bash

for i in *.jpg; do convert -verbose -flop "$i" "`echo $i | sed 's/.jpg/-converted.jpg/g'`"; done;
