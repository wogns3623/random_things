import cv2
import numpy as np
import math


# bgr_blue = np.uint8([[[255, 0, 0]]])
# bgr_green = np.uint8([[[0, 255, 0]]])
# bgr_red = np.uint8([[[  0, 0, 255]]])

# # hue(색) saturation(채도) value(진하기)
# hsv_blue = cv2.cvtColor(bgr_blue, cv2.COLOR_BGR2HSV)
# hsv_green = cv2.cvtColor(bgr_green, cv2.COLOR_BGR2HSV)
# hsv_red = cv2.cvtColor(bgr_red, cv2.COLOR_BGR2HSV)
# print(hsv_blue, hsv_green, hsv_red)

# hsv_black = np.uint8([[[123, 123, 0],[0, 123, 0],[123, 0, 0], [0, 0, 0]]])
# bgr_black = cv2.cvtColor(hsv_black, cv2.COLOR_HSV2BGR)
# hsv_black = cv2.cvtColor(bgr_black, cv2.COLOR_BGR2HSV)
# print(bgr_black, hsv_black, sep="\n")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

border = np.array(
    [[[(i * 6 - 3) * 10, 0, 0], [(i * 6 + 3) * 10, 255, 255]] for i in range(3)]
)

val = 0
def onChange(x): val = x
cv2.namedWindow("trackbar", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("blur", "trackbar", 0, 5, onChange)

while True:
    key = cv2.waitKey(1)
    if key != -1 and key == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break
    ret, frame = cap.read()
    cv2.imshow("video", frame)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blured = cv2.medianBlur(frame, val)
    blured_frame_hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
    for i in range(3):
        mask = cv2.inRange(blured_frame_hsv, border[i][0], border[i][1])
        # cv2.imshow(f"{i}", mask)
        mask_clean = cv2.morphologyEx(mask, cv2.morp, np.ones((3, 3), np.uint8))
        sep_frame = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow(f"{i}", sep_frame)
