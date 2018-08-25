from sklearn import preprocessing
from numpy import apply_along_axis

label_encoder = preprocessing.LabelEncoder()

labels = [
  "YOUR FLIGHTS",
  "SEAT OPTIONS", 
  "LUGGAGE OPTIONS",
  "SPECIAL ASSESTANCE",
  "FOOD AND DRINK",
  "NONE"
]

label_encoder.fit(labels)

def encodeLabels(data):
  return apply_along_axis(label_encoder.transform, 1,data)
