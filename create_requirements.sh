#!/bin/bash

REQ_FILE=requirements.txt

if [ -f $REQ_FILE ]; then
    rm $REQ_FILE
fi

pip freeze > $REQ_FILE