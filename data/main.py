from data import database
from data  import feature_preprocessor
import numpy

def getTransformedData():
  data = database.getTrainingData()
  return feature_preprocessor.encodeLabels(numpy.delete(data,0,1))

def getLabels():
  data = database.getTrainingData()
  return data[:,0]

def main():
  print(__name__)
