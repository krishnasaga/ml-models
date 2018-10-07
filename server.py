#Currently will source diff of features
#Get commit ids of source and destination branch from git repo
#Then get computer vision data collected at same commits
#Then get the feature diff of that collected data at two commits
 
from data import FeatureAccesser
from data.FeatureDiff import diffOfFeatures
from itertools import groupby
from flask import jsonify

from flask import Flask
app = Flask(__name__)

accesser = FeatureAccesser()

#Get source and destination branches hypersnapshots from elasticsearch
sourceResults = accesser.getFeaturesByCommit('ererer')

destinationResults = accesser.getFeaturesByCommit('5555')

#Cook results to served using feature diff

## as results given by elastic search are not grouped by senarios do som low budget code to group em
def keyFunc(doc):
    return doc["_source"]["senario"]

def groupDocs(sourceList,destiinationlist):
  sourceDocs = sourceResults["hits"]["hits"]
  destinationDocs = destinationResults["hits"]["hits"]
  return groupby(sorted(sourceDocs + destinationDocs,key=keyFunc),keyFunc)



diffsOfAllSenarios = []

for k,senario in groupDocs(sourceResults,destinationResults):
  diffGroup = list(senario)
  if(len(diffGroup) > 1):
    diffsOfAllSenarios.append({ "senario": k,
    "diff": diffOfFeatures(diffGroup[0]["_source"]["features"],
    diffGroup[1]["_source"]["features"])})
  else:
    diffsOfAllSenarios.append({ "senario": k,
    "diff": diffOfFeatures([],[])})

print(diffsOfAllSenarios)


#serve results as json
@app.route("/")
def hello():
    return jsonify(diffsOfAllSenarios)

if __name__ == '__main__':
  app.run('localhost', 5555)
 