import cv2
import numpy as np
import matplotlib.pyplot as plt

imgDir = "../image/"
def grad():
    img = cv2.imread(imgDir+"sana.jpg", cv2.IMREAD_GRAYSCALE)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap="gray")
    plt.title("original"), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap="gray")
    plt.title("laplacian"), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap="gray")
    plt.title("sobelx"), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap="gray")
    plt.title("sobely"), plt.xticks([]), plt.yticks([])

    plt.show()

def canny():
    img = cv2.imread(imgDir+"sana.jpg", cv2.IMREAD_GRAYSCALE)

    cv2.imshow("canny", img)

    val = [0, 200]
    def onChangeX(x):
        val[0] = x
        cv2.imshow("canny", cv2.Canny(img, val[0], val[1]))
    def onChangeY(y):
        val[1] = y
        cv2.createTrackbar("min", "trackbar", val[0], val[1], onChangeX)
        cv2.imshow("canny", cv2.Canny(img, val[0], val[1]))

    cv2.namedWindow("trackbar", cv2.WINDOW_AUTOSIZE)
    
    cv2.createTrackbar("min", "trackbar", 0, 200, onChangeX)
    cv2.createTrackbar("max", "trackbar", 200, 1000, onChangeY)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()