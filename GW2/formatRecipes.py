#!/usr/bin/python
import json
import sys

detail_file = open('recipe_details.json','r')
#created_file = open('recipe_created_items.json','r')

item_by_id=[]


created_items={}	#dictionary made by the created items JSON file
details = {} 	

with open('recipe_created_items.json') as data_file:    
	created_items = json.load(data_file)


with open('recipe_details.json') as data_file:    
	details = json.load(data_file)

i=1
while(True): 		#Loop over all recipes. We can't know how many there are beforehand
	recipe = details[str(i)]
	i+=1
	sys.stdout.write('"'+created_items[recipe['output_item_id']]['name']+'" '+recipe['output_item_count']+' "')
		#unfortunately, to be compatable with both python 2 and 3, to
		#add more to this line, I need to use sys.stdout.write()
	try:
		for ingredient in recipe['ingredients']:
			print ingredient['item_id']
			print created_items[int(str(ingredient['item_id']))]
			print ingredient['item_id']
			sys.stdout.write( '"'+created_items[ingredient['item_id']]['name']+'" ')
			sys.stdout.write( ingredient['count']+" ")
		print ""	
	except KeyError:
		continue

