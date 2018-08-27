from sklearn import tree
from data import preprocessing
##Classfy the bugs by looking at the page not by going deep into each feature
class PageBugClassfier:

    def __init__(self):
      self.classfier = tree.DecisionTreeClassifier()

    def __encodeFeatureLabels(data,d):
        encodedData = preprocessing.encodeFeatureLabels(data)
        return encodedData

    ##Accept a two dymentional array of strings ( categorical data )
    def fit(self,trainingData):
        encodedTrainingData = self.__encodeFeatureLabels(trainingData)
        self.classfier.fit(encodedTrainingData,["one"])

    ##Accept a two dymentional array of strings ( categorical data )
    def predict(self,testData):
        encodedTestData = self.__encodeFeatureLabels(trainingData)
        predictions = self.calssfier.predict(encodedTestData)
        return predictions
