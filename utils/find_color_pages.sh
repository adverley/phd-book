#!/bin/bash


if [ $# -ne 1 ] 
then
    echo "USAGE: This script needs exactly one paramter: the path to the PDF"
    kill -SIGINT $$
fi

FILE=$1

# gs -o - -sDEVICE=inkcov $FILE |tail -n +4 |sed '/^Page*/N;s/\n//'|sed -E '/Page [0-9]+ 0.00000  0.00000  0.00000  / d' > colorOnly.log
gs -o - -sDEVICE=inkcov $FILE |tail -n +4 |sed '/^Page*/N;s/\n//' > color.log
