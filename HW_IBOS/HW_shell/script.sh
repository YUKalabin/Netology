#!/bin/bash
if [$# -eq 2]
then    
    if [$1 = "crypt"]
    then
        echo $2 | base64
        exit 0
    elif [ $1 = "decrypt" ]
    then
        echo $2 | base64 -d
        exit 0
    else
        echo "Wrong paremetr"
        exit 1
    fi
else
    echo "The number of parameters is not equal to 2"
    exit 1
fi