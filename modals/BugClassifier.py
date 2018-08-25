from data import main
from sklearn import tree
from data import feature_preprocessor
from numpy import apply_along_axis

training_data = main.getTransformedData()
training_labels = main.getLabels()

class BugClassifier:
  def __init__(self):
    self.clf = tree.DecisionTreeClassifier()

  def fit(self,data,labels):
    return self.clf.fit(apply_along_axis(feature_preprocessor.label_encoder.transform, 1,data),labels)

  def predict(self,data):
    return self.clf.predict(apply_along_axis(feature_preprocessor.label_encoder.transform, 1,data))
