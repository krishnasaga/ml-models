
import json
from deepdiff import DeepDiff

#Gives diff between source to destination
def diffFeatures(sourceResults,destinationResults):
 diffdata =   eepDiff(sourceResults, destinationResults, exclude_paths={"root['match']"})
 return diffdata
