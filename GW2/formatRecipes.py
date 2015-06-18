#!/usr/bin/python
import json
import sys

#detail_file = open('recipe_details.json','r')
#created_file = open('recipe_created_items.json','r')

item_by_id=[]


created_items={}	#dictionary made by the created items JSON file
details = {}

with open('recipe_created_items.json') as data_file:
	created_items = json.load(data_file)


with open('recipe_details.json') as data_file:
	details = json.load(data_file)

for i in details.keys(): 		#Loop over all recipes. We can't know how many there are beforehand
	recipe = details[str(i)]
	out = '"@'+recipe['output_item_id']+'"@ '+recipe['output_item_count']+' '	#save by item id
												#save by item name
	#out = '"@'+created_items[recipe['output_item_id']]['name']+'"@ '+recipe['output_item_count']+' '	
	try:
		for ingredient in recipe['ingredients']:
			out+= '"@'+ingredient['item_id']+'"@ '	#save by item id
			#out+= '"@'+created_items[ingredient['item_id']]['name']+'"@ '	#save by item name
			out+= ingredient['count']+" "
			
			#sys.stdout.write( '"'+created_items[ingredient['item_id']]['name']+'" ')
			#sys.stdout.write( ingredient['count']+" ")
	except KeyError:
		continue
	print out

print ""	
