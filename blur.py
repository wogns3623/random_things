import cv2
import numpy as np
import math


src = cv2.imread("./image/sana.jpg")
cv2.imshow("sana", src)
val = [0, 0, 0]

def draw():
    cv2.imshow("blur1", cv2.blur(src, (val[0], val[0])))
    cv2.imshow("blur2", cv2.GaussianBlur(src, (val[0], val[0]), 0))
    cv2.imshow("blur3", cv2.medianBlur(src, val[0]))
    cv2.imshow("blur4", cv2.bilateralFilter(src, val[0], val[1], val[2]))

def onChange1(x):
    val[0] = x+1
    draw()
def onChange2(x):
    val[1] = x+1
    draw()
def onChange3(x):
    val[2] = x+1
    draw()
    
cv2.namedWindow("trackbar", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("blurVal", "trackbar", 0, 20, onChange1)
cv2.createTrackbar("blurVal1", "trackbar", 0, 100, onChange2)
cv2.createTrackbar("blurVal2", "trackbar", 0, 100, onChange3)


cv2.waitKey(0)
cv2.destroyAllWindows()