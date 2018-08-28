import cv2

image = cv2.imread('./someimage.jpg')

ret,thresh = cv2.threshold(image,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cv2.imshow('Hello, World!',image)

cv2.waitKey(33)
