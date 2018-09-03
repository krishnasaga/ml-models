import cv2 as opencv
import numpy as np
class RectangleDetector:

  def isRectangle(self,curve):
      peri = opencv.arcLength(curve, True)
      approx = opencv.approxPolyDP(curve, 0.01 * peri, True)
      return len(approx) == 4

  def detect(self,image):
      imgray = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
      ret,thresh = opencv.threshold(imgray,240,255,0)
      im2, rectangles,heighercy = opencv.findContours(thresh,opencv.RETR_TREE,opencv.CHAIN_APPROX_SIMPLE)
      __rectangles = np.array(filter(self.isRectangle,rectangles))
      return __rectangles,thresh
