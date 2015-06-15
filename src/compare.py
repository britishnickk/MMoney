#!/usr/bin/python

#Need dictionary of items/prices, array of recipes

items={}

print "Please enter one item per line in the following format:"
print "\"[item]\" [price]"
print "Enter an empty line to finish \n"

#Read in items
while(True):
	itemPrice = raw_input()
	if itemPrice == "":
		break
	itemPrice= itemPrice.split('"')
	if len(itemPrice) < 3 :
		print "All items must have a price"
	else:
		item = itemPrice[1]
		price = itemPrice[2]
		items[item] = price

#print "\n-----------------RECIPES------------------"
#Read in Recipes
recipes=[]
while(True):
	itemRecipe = raw_input()
	if itemRecipe == "":
		break
	itemRecipe= itemRecipe.split('"')

	item = itemRecipe[1]
	recipe = itemRecipe[1:]

	recipes.append(recipe)


data = []
#print "------------------Calculating Profits-----------------"
for recipe in recipes:
#	print "Calculating for:"+str(recipe)
#	print ""
	product = int(recipe[1]) * int(items[recipe[0]])
	for i in range(2,len(recipe)):
		if i%2 == 1:
			continue
		product = product - int(recipe[i+1]) * int(items[recipe[i]])
#	print "Profit for making "+str(recipe[0])+" is "+str(product)	
	data.append((product,recipe))
data=sorted(data,reverse=True)

top=5
top = min(top,len(data))
print "The top "+str(top)+" most profitable recipies are:"
for i in range(top):
	print "For $"+str(data[i][0])+" craft "+ str(data[i][1][1])+" "+str(data[i][1][0])+" using:"
	for j in range(2,len(data[i][1])):
		if j%2==1:
			continue
		print ""+str(data[i][1][j+1])+" "+str(data[i][1][j])	
	


















