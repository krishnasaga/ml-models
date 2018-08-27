from models.PageBugClassfier import PageBugClassfier
import numpy as np

classfier = PageBugClassfier()

classfier.fit(np.array([
  ["Valid","ONE","TWO","THREE"],
  ["INVALID","ONE","THREE","FIVE"],
  ["INVALID","ONE","FOUR","THREE"],
  ["INVALID","ONE","TWO","FOUR"]
]))

predections = classfier.predict([["ONE","THREE","ONE"]])

print(predections)
