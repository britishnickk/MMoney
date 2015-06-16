#!/bin/bash
BASEDIR=$(dirname $0)
wget -q http://gw2spidy.com/api/v0.9/csv/all-items/all -O $BASEDIR/rawItems.txt
