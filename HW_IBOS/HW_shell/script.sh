#!/bin/bash
if [ $# -eq 2 ]
then    
    if [ $1 = "crypt" ]
    then
        echo $2 | base64
        exit
    elif [ $1 = "decrypt" ]
    then
        echo $2 | base64 -d
        exit
    else
        echo "Wrong parametr"
        exit 1
    fi
else
    echo "The number of parameters is not equal to 2"
    exit 1
fi
