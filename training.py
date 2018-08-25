import numpy
from sklearn import preprocessing

labels = [
  "YOUR FLIGHTS",
  "SEAT OPTIONS", 
  "LUGGAGE OPTIONS",
  "SPECIAL ASSESTANCE",
  "FOOD AND DRINK"
]

trainingData = [
 ["YOUR FLIGHTS","SEAT OPTIONS","LUGGAGE OPTIONS","SPECIAL ASSESTANCE","FOOD AND DRINK"]
]

trainingLables = [
  "VALID","INVALID"
]

encoder = preprocessing.LabelEncoder()
encoder.fit(labels)

def getLabels():
  encoder.transform(numpy.array(labels))

def getTrainingData():
  numpy.apply_along_axis(encoder.transform,1,numpy.array(trainingData))

def getTrainingLables():
  numpy.array(trainingLables)
