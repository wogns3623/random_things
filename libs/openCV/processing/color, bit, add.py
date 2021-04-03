import cv2
import numpy as np


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print(x, y)


cv2.namedWindow("trackbar", cv2.WINDOW_AUTOSIZE)

# read Image
imgDir = "../image/"
image = cv2.imread(imgDir+"babaisyou.jpg", cv2.IMREAD_ANYCOLOR)
src = cv2.imread(imgDir+"test.jpg", cv2.IMREAD_ANYCOLOR)

cv2.imshow("baba", image)
cv2.setMouseCallback("baba", onMouse)


# BGR         |	Blue, Green, Red 채널           | -
# BGRA        | Blue, Green, Red, Alpha 채널    | -
# RGB         |	Red, Green, Blue 채널           | -
# RGBA        | Red, Green, Blue, Alpha 채널    | -
# GRAY        | 단일 채널                       | 그레이스케일
# BGR565      | Blue, Green, Red 채널           | 16 비트 이미지
# XYZ         | X, Y, Z 채널                    | CIE 1931 색 공간
# YCrCb       |	Y, Cr, Cb 채널                  | YCC (크로마)
# HSV         |	Hue, Saturation, Value 채널     | 색상, 채도, 명도
# Lab         |	L, a, b 채널                    | 반사율, 색도1, 색도2
# Luv         |	L, u, v 채널                    | CIE Luv
# HLS         |	Hue, Lightness, Saturation 채널 |	색상, 밝기, 채도
# YUV         |	Y, U, V 채널                    | 밝기, 색상1, 색상2
# BG, GB, RG  | 디모자이킹                      |	단일 색상 공간으로 변경
# _EA         | 디모자이킹                      | 가장자리 인식
# _VNG        | 디모자이킹	                    | 그라데이션 사용
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("grey Baba", grey)


# image_r = image[:, :, 2]
# image_g = image[:, :, 1]
# image_b = image[:, :, 0]
# cv2.imshow("r Baba", image_r)
# cv2.imshow("g Baba", image_g)
# cv2.imshow("b Baba", image_b)

# image_copy = image.copy()
# image_copy[:, :, :2] = 0
# cv2.imshow("baba is red", image_copy)


# not1 = cv2.bitwise_not(image)
# cv2.imshow("not Baba", not1)
# or1 = cv2.bitwise_or(image, cv2.flip(image, 1))
# cv2.imshow("abaB and Baba", or1)
# binRet, bin1 = cv2.threshold(grey, 100, 225, cv2.THRESH_BINARY)
# cv2.imshow("01 Baba", bin1)

keke = image[149:222, 13:80]
# cv2.imshow("keke", keke)

kekebg = np.zeros(src.shape, np.uint8)
lh = (src.shape[0] - keke.shape[0]) // 2
lw = (src.shape[1] - keke.shape[1]) // 2
kekebg[lh : lh + keke.shape[0], lw : lw + keke.shape[1]] = keke

src_c = src.copy()
src_c[lh : lh + keke.shape[0], lw : lw + keke.shape[1]] = keke

# cv2.imshow("add0", src_c)
# cv2.imshow("add1", cv2.bitwise_or(src, kekebg))
# cv2.imshow("add2", cv2.add(src, kekebg))
# cv2.imshow("add3", src+kekebg)


# get mask, keke with black bg
keke_grey = cv2.cvtColor(keke, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(keke_grey, 20, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

bg = src[lh : lh + keke.shape[0], lw : lw + keke.shape[1]]
bg_mask = cv2.bitwise_and(bg, bg, mask=mask_inv)
keke_black_bg = cv2.bitwise_and(keke, keke, mask=mask)
keke_with_bg = cv2.add(bg_mask, keke_black_bg)

# cv2.imshow("1", keke)
# cv2.imshow("2", bg)
# cv2.imshow("3", keke_grey)
# cv2.imshow("4", mask)
# cv2.imshow("5", mask_inv)
# cv2.imshow("6", bg_mask)
# cv2.imshow("7", keke_black_bg)
# cv2.imshow("8", keke_with_bg)
keke_bg = src.copy()
keke_bg[lh : lh + keke.shape[0], lw : lw + keke.shape[1]] = keke_with_bg
cv2.imshow("keke in img", keke_bg)


# blend baba to keke
baba = image[149:222, 112 : 112 + keke.shape[1]]
# cv2.imshow("only baba", baba)

baba_grey = cv2.cvtColor(baba, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(baba_grey, 67, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

baba_without_bg = cv2.bitwise_and(baba, baba, mask=mask)
bg_without_baba = cv2.bitwise_and(baba, baba, mask=mask_inv)

# cv2.imshow("6", baba_without_bg)
# cv2.imshow("7", bg_without_baba)

# erode and dilate => remove noise
# improvement version : morphologyEx
kernel = np.ones((2, 2), np.uint8)
# bg_without_baba = cv2.erode(bg_without_baba, kernel, iterations=1)
# bg_without_baba = cv2.dilate(bg_without_baba, kernel, iterations=1)
bg_without_baba = cv2.morphologyEx(bg_without_baba, cv2.MORPH_OPEN, kernel)

# cv2.imshow("8", bg_without_baba)

# modified = cv2.add(bg_without_baba, baba_without_bg)
# cv2.imshow("9", modified)

# bg_with_keke = cv2.add(bg_without_baba, keke)
# cv2.imshow("9", bg_with_keke)

bg_remove_baba = image.copy()

baba2keke = cv2.addWeighted(baba_without_bg, 1, keke, 0, 0)
bg_remove_baba[149:222, 112 : 112 + keke.shape[1]] = baba2keke
cv2.imshow("baba is keke", bg_remove_baba)


def handleTrackbar2(x):
    baba2keke = cv2.addWeighted(baba_without_bg, (100 - x) / 100, keke, x / 100, 0)
    baba2keke = cv2.add(bg_without_baba, baba2keke)
    bg_remove_baba[149:222, 112 : 112 + keke.shape[1]] = baba2keke
    cv2.imshow("baba is keke", bg_remove_baba)


cv2.createTrackbar("blend", "trackbar", 0, 100, handleTrackbar2)


# wait until any key input
cv2.waitKey(0)
# if read key input, destroy all windows
cv2.destroyAllWindows()
