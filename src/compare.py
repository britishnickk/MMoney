#!/usr/bin/python

#Need dictionary of items/prices, array of recipes

items={}

print "Please enter one item per line in the following format:"
print "\"[item]\" [instant sell price] [instant buy price]"
print "Enter an empty line to finish \n"

#Read in items
itemPrice = raw_input()
itemPrice = raw_input()
while(True):
	itemPrice = raw_input()
	if '"' not in itemPrice:# == "":
		break
	itemPrice= itemPrice.split('"@')
	if len(itemPrice) < 3 :
		print "All items must have a price"
		print "\tYou entered: "+str(itemPrice)
	else:
		item = str(itemPrice[1])
		prices = (itemPrice[2]).split(' ')
		price=prices[1]
		maxprice=int(prices[2])
		items[item] = price
		print "Item "+str(item)+" costs "+ str(price)

print "\n-----------------PARSING RECIPES------------------"
#Read in Recipes
recipes=[]
while(True):
	itemRecipe = raw_input()
	if itemRecipe == "":
		break
	itemRecipe= itemRecipe.split('"@')
	if len(itemRecipe) < 4:
		print "Invalid Recipe: " + str(itemRecipe)
		exit()
	item = itemRecipe[1]
	recipe = itemRecipe[1:]
	recipes.append(recipe)


data = []
for item in items:
	print "Key: "+str(item)+" Value: "+str(items[item])
print "------------------Calculating Profits-----------------"
for recipe in recipes:
	print "Calculating for:"+str(recipe)
#	print ""
	product=0
	try:
#		print "recipe[1] = "+ recipe[1]
#		print "items[recipe[0]] = "+ items[recipe[0]]
		product = int(recipe[1]) * int(items[recipe[0]])
#		print "Net gain: "+str(product)	
		for i in range(2,len(recipe)):
			if i%2 == 1:
				continue
			product = product - int(recipe[i+1]) * int(items[recipe[i]])
		print "Profit for making "+str(recipe[0])+" is "+str(product)	
		data.append((product,recipe))
	except KeyError:	#Recipe requires unknown item. Continue to next recipe.
		continue
#	except ValueError:
#		continue
	except KeyboardInterrupt:
		exit()

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
	


















