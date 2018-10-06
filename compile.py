from cv import TemplateDetect
import os

templateDetect = TemplateDetect()
templateDetect.setTemplates(os.getcwd()+'/')

matches = templateDetect.detect(os.getcwd() +'/')

print(matches[0].position)
