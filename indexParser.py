import json

kibanaFile = open("export.json", "r+").read()
outputFile = open("output.txt", "w")

j = json.loads(kibanaFile)

for i, value in enumerate(j):
	if "index" in j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']:
		#print "yes"
		#print j[i]['_source']['title']
		title = j[i]['_source']['title']
		

		if '2018.3' in title:
				#print "yes .2"
				#print j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']
			print title

			searchsource = json.loads(j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON'])
			if '183' not in searchsource["index"]:

				index = searchsource["index"]
				print index
				index = index[:-3]
				index = index + "183"
				searchsource["index"] = index
				j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON'] = searchsource
				print index

newExport = open("newExport.json", "w")
newExport.write(str(j))
newExport.close()

lol = open("newExport.json")

outputFile.close()
