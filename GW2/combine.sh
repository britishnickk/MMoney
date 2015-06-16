#!/bin/bash
BASEDIR=$(dirname $0)
cat $BASEDIR/items.txt > $BASEDIR/both.txt
cat $BASEDIR/recipes.txt >> $BASEDIR/both.txt
