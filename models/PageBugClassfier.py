from sklearn import tree
from data import processing
import numpy as np

class Predection:
    def __init__(self,answer):
        self.answer = answer

##Classfy the bugs by looking at the page not by going deep into each feature
class PageBugClassfier:

    def __init__(self):
      self.classfier = tree.DecisionTreeClassifier()

    def __encodeFeatureLabels(data,d):
        encodedData = processing.encodeFeatureLabels(data)
        return encodedData

    ##Accept a two dymentional array of strings ( categorical data )
    def fit(self,trainingData):

        ##extracting and encoding labels
        labels = processing.extractFeatueLabels(trainingData)

        ##extracting and decodeing data
        ##this extracting is just removing first column ( feature labels )
        extractedTrainingData = processing.extractData(trainingData)
        encodedTrainingData = processing.encodeData(extractedTrainingData)

        self.classfier.fit(encodedTrainingData,labels)

    ##Accept a two dymentional array of strings ( categorical data )
    def predict(self,testData):
        encodedTestData = processing.encodeData(testData)
        predictions = self.classfier.predict(encodedTestData)
        return np.vectorize(Predection)(predictions)

    ##Predections score
    def score(self,testData):
        encodedTestData = processing.encodeData(testData)
        predictions = self.classfier.predict(encodedTestData)
        return predictions
