import os
from cv import CVCollector

cvcollector = CVCollector(os.getcwd()+'/ml-models',os.getcwd()+'/ml-models')

results = cvcollector.collect()

print(results)
