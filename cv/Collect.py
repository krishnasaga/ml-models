from cv import TemplateDetect
import os
from os import listdir
from os.path import isfile, join

def getAllScreenshotsInPath(path):
   onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
   return map(lambda filePath: path+filePath,onlyfiles)

class CVCollector:
  def __init__(self,traningPath,screenShotsPath):
    self.traningPath = traningPath
    self.screenshotsPath = screenShotsPath
    self.templateDetect = TemplateDetect()
    self.templateDetect.setTemplates(self.traningPath)

  def collect(self):
    screenshotPaths = getAllScreenshotsInPath(self.screenshotsPath)
    return map(self.templateDetect.detect,screenshotPaths)
