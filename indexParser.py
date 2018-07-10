import json

kibanaFile = open("export.json", "w")

j = json.loads(kibanaFile)

print j["_id"]