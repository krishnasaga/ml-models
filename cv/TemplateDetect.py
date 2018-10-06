import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join
from time import sleep

class Feature:
  def __init__(self,name,template):
    self.name = name
    self.template = template

class Match:
  def __init__(self,match,position):
    self.match = match
    self.position = position

def readFeatureTemplate(path):
  template = cv.imread(path,0)
  return Feature(path,template)

def __isValidFeatures(featue):
  return featue.template is not None

def getAllFeaturesInDirectory(path):
  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  allFeatures = map( lambda f: readFeatureTemplate(path+'/'+f),onlyfiles)
  validFeatures = filter(__isValidFeatures ,allFeatures)
  return validFeatures

#Detect all features in a given screenshots
def getFeatureMatchOfGivenScreenShot(feature,screenShot):
  w, h = feature.template.shape[::-1]
  res = cv.matchTemplate(screenShot,feature.template,cv.TM_CCORR_NORMED)
  min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
  return Match(1,[max_loc,max_loc[0] + w, max_loc[1] + h])

def getAllMatcheingFeaturesInAGivenScreenShot(features,screenShot):
  screenShotImage = cv.imread(screenShot,0)
  if hasattr(cv,'shape'):
    return map( lambda f: getFeatureMatchOfGivenScreenShot(f,screenShotImage),features)
  return []
  

#To find all features in a given screen shot
class TemplateDetect:
  
  #set template directory befor starting detect
  def setTemplates(self,templatePath):
    self.templatesPath = templatePath

  #find all features in given template directory
  def detect(self,screenShot):
    features = getAllFeaturesInDirectory(self.templatesPath)
    print(features)
    return getAllMatcheingFeaturesInAGivenScreenShot(features,screenShot)
