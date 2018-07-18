import json
import sys

with open("export.json", "r+") as kibanaFile:
	#outputFile = open("output.txt", "w")

	j = json.load(kibanaFile)
	kibanaFile.close()

	for i, value in enumerate(j):
		if "index" in j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON']:
			title = j[i]['_source']['title']
			
			if sys.argv[1] in title:
				searchsource = json.loads(j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON'])
				indexNum = sys.argv[1].replace(".", "")[2:]

				if indexNum not in searchsource["index"]:
					index = searchsource["index"]
					#print index
					index = index[:-3]
					index = index + indexNum
					searchsource["index"] = index
					j[i]['_source']['kibanaSavedObjectMeta']['searchSourceJSON'] = searchsource

	kibanaFile = open('export.json', "w")
	json.dump(j, kibanaFile)
	kibanaFile.close()
