#!/bin/bash 
COUNTER=2010

source venv/bin/activate
while [  $COUNTER -lt 2015 ]; do
    heroku run python manage.py import_raw_data $COUNTER $COUNTER --toxic --air
    let COUNTER+=1
done
