#!/usr/bin/python

prices={}
with open('rawItems.txt') as f:
	while(True):
		line=f.readline().split(',')
		if len(line)<10:
			print len(line)
			print line
			break;
		prices[line[1]]= [line[8],line[9]]

for item in prices:
	print item+" " + prices[item][0] + " " + prices[item][1]
print ""
