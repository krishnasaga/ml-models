from cv import TemplateDetect
import os

templateDetect = TemplateDetect()
templateDetect.setTemplates(os.getcwd()+'/ml-models/')

matches = templateDetect.detect(os.getcwd() +'/ml-models/')

print(matches[0].position)
