from sklearn import preprocessing

#Encodes feature labels to numerical values especially useful for DecisionTreeClassifier
def encodeFeatureLabels(data):
    encoder = preprocessing.labelEncoder()
    encoder.fit([""])
    encodedData = encoder.transform(data)
    return encodedData

#Takes numpy array as input
def extractFeatueLabels(data):
    features = data[1:,:]
