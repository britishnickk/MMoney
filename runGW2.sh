#!/bin/bash
BASEDIR=$(dirname $0)
$BASEDIR/GW2/getItems.sh
$BASEDIR/GW2/formatPrices.py > $BASEDIR/GW2/items.txt
$BASEDIR/GW2/formatRecipes.py > $BASEDIR/GW2/recipes.txt
$BASEDIR/GW2/combine.sh
cat $BASEDIR/GW2/both.txt | $BASEDIR/GW2/compare.py
#rm $BASEDIR/GW2/both.txt
