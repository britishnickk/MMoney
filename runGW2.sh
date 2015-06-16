#!/bin/bash
BASEDIR=$(dirname $0)
$BASEDIR/GW2/combine.sh
cat $BASEDIR/GW2/both.txt | $BASEDIR/src/compare.py
rm $BASEDIR/GW2/both.txt
