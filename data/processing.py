from sklearn import preprocessing
import numpy as np

#Encodes feature labels to numerical values especially useful for DecisionTreeClassifier
def encodeFeatureLabels(data):
    encoder = preprocessing.LabelEncoder()
    encoder.fit(data)
    encodedData = encoder.transform(data)
    return encodedData

def encodeData(data):
    encodedData = np.apply_along_axis(encodeFeatureLabels,1,data)
    return encodedData

#Takes numpy array as input
def extractFeatueLabels(data):
    featureLabels = data[:,0]
    return featureLabels

def extractData(data):
    _data = data[:,1:]
    return _data
