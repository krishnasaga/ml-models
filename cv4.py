import cv2 as opencv
import sys
from cv import RectangleDetector

scriptName = sys.argv[0]
inputdir = sys.argv[1]
commithash = sys.argv[2]
outputdir = sys.argv[3]

image = opencv.imread(inputdir+'/flight-options.png')

rectangleDetector = RectangleDetector()
rectangles,thresh = rectangleDetector.detect(image);

outputimage = opencv.drawContours(image, rectangles, -1, (0,255,0), 3)

opencv.imwrite(outputdir + '/1.png',outputimage)
opencv.imwrite(outputdir + '/2.png',thresh)
