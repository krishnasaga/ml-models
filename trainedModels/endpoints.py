from models.PageBugClassfier import PageBugClassfier
import numpy as np

pageBugClassfier =  PageBugClassfier()

pageBugClassfier.fit(np.array([
  ["Valid","ONE","TWO","THREE"],
  ["INVALID","ONE","THREE","FIVE"],
  ["INVALID","ONE","FOUR","THREE"],
  ["INVALID","ONE","TWO","FOUR"],
  ["INVALID","THREE","THREE","THREE"]
]))
