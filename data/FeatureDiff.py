
class Feature:
  def __init__(self,name):
    self.name = name
  
  def __hash__(self):
    return hash(self.name)
 
  def __eq__(self, other):
    return self.name == other.name
 
#Because dicts are not elegible for creating sets
def toFeatures(feature):
    return Feature(feature["name"])

#Features that added in agiven senario
def addedFeatures(sourceFeatures,destinationFeatures):
   sourceSet = set(map(toFeatures,sourceFeatures))
   destinationSet = set(map(toFeatures,destinationFeatures))
   return sourceSet.difference(destinationSet)

#Removed features in a given senario
def removedFeatures(sourceFeatures,destinationFeatures):
   sourceSet = set(map(toFeatures,sourceFeatures))
   destinationSet = set(map(toFeatures,destinationFeatures))
   return destinationSet.difference(sourceSet)

#Diff features in a given senario in terms of added and removed
def diffOfFeatures(sourceFeatures,destinationFeatures):
    added = addedFeatures(sourceFeatures,destinationFeatures)
    removed = removedFeatures(sourceFeatures,destinationFeatures)
    return { "added": list(added), "removed": list(removed) }
