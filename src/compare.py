#!/usr/bin/python

#Need dictionary of items/prices, array of recipes

items={}

print "Please enter one item per line in the following format:"
print "\"[item]\" [price]"
print "Enter an empty line to finish \n"

while(True):
	itemPrice = raw_input("-->")
	if itemPrice == "":
		break
	itemPrice= itemPrice.split('"')
	if len(itemPrice) < 2 :
		print "All items must have a price"
	else:
		item = itemPrice[1]
		price = itemPrice[2]
		items[item] = price

		print ""+item+" costs "+items[item]
