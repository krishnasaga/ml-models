from elasticsearch import Elasticsearch

class FeatureAccesser:
   def __init__(self):
     self.es = Elasticsearch()

   def getFeaturesByCommit(self,commithash):
     return self.es.search(
         index="computer-vision-data",
         body={"query": {"match": {
           "commithash": commithash
         }}})
