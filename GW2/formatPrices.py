#!/usr/bin/python

prices={}
with open('rawItems.txt') as f:
	f.readline()
	while(True):
		line=f.readline().split(',')
		if len(line)<10:
			print len(line)
			print line
			break;
		
		prices[line[0]]= [line[-6],line[-5]]	#save by item id
		#prices[line[1]]= [line[-6],line[-5]	#save by item name]

for item in prices:
	print "\"@"+item+"\"@ " + prices[item][0] + " " + prices[item][1]
	#print "\"@ "+item[1:]+"@ " + prices[item][0] + " " + prices[item][1]	#use when saving item by name
print ""
