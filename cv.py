import cv2 as opencv
from cv import RectangleDetector

image = opencv.imread('./cvio/input/1.png')

rectangleDetector = RectangleDetector()
rectangles,thresh = rectangleDetector.detect(image);

outputimage = opencv.drawContours(image, rectangles, -1, (0,255,0), 3)

opencv.imwrite('./cvio/output/1.png',outputimage)
opencv.imwrite('./cvio/output/2.png',thresh)
