import json

kibanaFile = open("export.json", "r+").read()
outputFile = open("output.txt", "w")

j = json.loads(kibanaFile)

for i, value in enumerate(j):
	if "index" in j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']:
		#print "yes"
		#print j[i]['_source']['title']
		title = j[i]['_source']['title']
		

		if '-' in title:
			#print "yes -"
			if '2018.2' in title:
				#print "yes .2"
				#print j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']

				searchsource = json.loads(j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON'])
				if '182' in searchsource["index"]:
					print searchsource["index"]
					print title
					
				else:
					print "invalid index"
					outputFile.write(title + "\n")
					outputFile.write(searchsource["index"] + "\n")
					outputFile.write("\n")
					outputFile.write("invalid index\n")
					outputFile.write("\n")


		#print j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']["index"]
			#check title name
		#if the title and index arent equal
		#change the index to reflect the title
	else:
		print "no"
outputFile.close()
