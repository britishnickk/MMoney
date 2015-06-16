#!/bin/bash
BASEDIR=$(dirname $0)
$BASEDIR/test/combine.sh
cat $BASEDIR/test/both.txt | $BASEDIR/src/compare.py
rm $BASEDIR/test/both.txt
