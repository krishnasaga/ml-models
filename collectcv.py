import os
from cv import CVCollector

from datetime import datetime
from elasticsearch import Elasticsearch


#screen shot details
trainingPath = os.getcwd()+'/templ/'
screenshotsPath = os.getcwd()+'/cvio/input/'

#elasticsearch details
username = 'username'
password = 'password'
host = 'localhost'

cvcollector = CVCollector(trainingPath,screenshotsPath)

results = cvcollector.collect()

#stash them in elasticsearch
docs = map( lambda result: {
  "features": map(lambda feature: { "position": feature.position },result)
},results)
print(docs)

currentId = datetime.now()
es = Elasticsearch()
for doc in docs:
  res = es.index(index="computer-vision-data", doc_type='matches', id=currentId, body=doc)
  print(res)
