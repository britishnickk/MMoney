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
	out = '"'+created_items[recipe['output_item_id']]['name']+'" '+recipe['output_item_count']+' "'
	#sys.stdout.write('"'+created_items[recipe['output_item_id']]['name']+'" '+recipe['output_item_count']+' "')
		#unfortunately, to be compatable with both python 2 and 3, to
		#add more to this line, I need to use sys.stdout.write()
	try:
		for ingredient in recipe['ingredients']:
			out+= '"'+created_items[ingredient['item_id']]['name']+'" '
			out+= ingredient['count']+" "
			
			#sys.stdout.write( '"'+created_items[ingredient['item_id']]['name']+'" ')
			#sys.stdout.write( ingredient['count']+" ")
	except KeyError:
		continue
	print out

print ""	
