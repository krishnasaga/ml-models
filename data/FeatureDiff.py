import FeatureAccesser

import json
from pprint import pprint
from deepdiff import DeepDiff

with open('./cvio/input/file.txt') as first:
  firstData = json.load(first)    
with open('./cvio/input/file1.txt') as second: 
   secondData = json.load(second)

print (DeepDiff(firstData, secondData, exclude_paths={"root['match']"}))