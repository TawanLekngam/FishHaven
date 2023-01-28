#!/bin/bash

REQ_FILE=requirements.txt

if [ -f $REQ_FILE ]; then
    pip install -r $REQ_FILE
else
    echo "Error: $REQ_FILE not found"
fi
