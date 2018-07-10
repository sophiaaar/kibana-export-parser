import json

kibanaFile = open("export.json", "r+").read()

j = json.loads(kibanaFile)

for index, value in enumerate(j):
	print j[index]['_id']
	#if index exists
	#check title name
	#if the title and index arent equal
	#change the index to reflect the title