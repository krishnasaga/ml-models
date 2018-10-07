import os
from cv import CVCollector

from datetime import datetime
from elasticsearch import Elasticsearch
import sys
import json

#low budget code to read command line args
arg_names = ['programname','commithash']
args = dict(zip(arg_names, sys.argv))

#read configuratin from json
if(os.environ.get('DOMAIN_COMPILER_HOME') is None):
  print('You have to set DOMAIN_COMPILER_HOME first')
  exit(1)

with open(os.environ['DOMAIN_COMPILER_HOME']+'/config.json') as f:
    config = json.load(f)

#screenshot details
trainingPath = config["trainingPath"]
screenshotsPath = config["screenshotsPath"]

#elasticsearch details
username = 'username'
password = 'password'
host = 'localhost'

#Git data from command line args
commithash = args['commithash']
print(commithash)

#collect computer vision data from screenshots
cvcollector = CVCollector(trainingPath,screenshotsPath)

results = cvcollector.collect()

#stash them in elasticsearch
docs = map(lambda result: { "senario": result["senario"],"features": map(lambda f: {
  "name": f.feature.name,
  "position": f.position
},result["features"]) },results)

print(docs)

currentId = datetime.now()
es = Elasticsearch()
for doc in docs:
  res = es.index(index="computer-vision-data", 
    doc_type='matches',
    id=commithash + doc["senario"], 
    body=doc)
  print(res)
