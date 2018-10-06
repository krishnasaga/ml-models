import os
from cv import CVCollector

cvcollector = CVCollector(os.getcwd()+'/templ/',os.getcwd()+'/cvio/input/')

results = cvcollector.collect()

print(results[1][0].position)
 