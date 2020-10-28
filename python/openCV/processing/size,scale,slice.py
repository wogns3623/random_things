import cv2
import numpy as np
import math as m

# read Image
imgDir = "../image/"
image = cv2.imread(imgDir+"babaisyou.jpg", cv2.IMREAD_ANYCOLOR)
height, width, channel = image.shape
print(
    f"height is {height}\n\
width is {width}\n\
channel is {channel}"
)

# create window containing img
# this window doesn't support resizing
cv2.imshow("baba", image)

# if flip's second var >=1 then left-right flip
# else if  <= 0 then up-down flip
# then, 0 < < 1 ==> only int!
cv2.imshow("flip Baba", cv2.flip(image, 0))

# center, degree, scale
degree = 90
mat = cv2.getRotationMatrix2D((width, 0), degree, 1)
cp = m.pi / 180 * (degree)
rotatedH = round(m.cos(cp) * height + m.sin(cp) * width)
rotatedW = round(m.sin(cp) * height + m.cos(cp) * width)
mW = width - (round(m.cos(cp) * width) + 1)
rotated = cv2.warpAffine(image, mat, (rotatedW + mW, rotatedH))[:, mW:]
cv2.imshow("rotated Baba", rotated)

# image, retVar, size, border_type
# border_type only allow cv2.BORDER_DEFAULT
# only *2, /2 resizing support
big = cv2.pyrUp(image, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
small = cv2.pyrDown(
    image, dstsize=(width // 2, height // 2), borderType=cv2.BORDER_DEFAULT
)
cv2.imshow("big Baba", big)
cv2.imshow("small Baba", small)

# if resize image bigger, use INTER_CUBIC or INTER_LINEAR
# else if smaller, use INTER_AREA
# INTER_AREA -> bigger, use INTER_NEAREST
# dsize have more priority then fx, fy
resize1 = cv2.resize(image, dsize=(300, 300), interpolation=cv2.INTER_AREA)
resize2 = cv2.resize(
    image, dsize=(0, 0), fx=0.5, fy=0.7, interpolation=cv2.INTER_LINEAR
)
cv2.imshow("resize Baba1", resize1)
cv2.imshow("resize Baba2", resize2)

# # 걍 리스트 짤라서 갖다붙인거
sliced1 = image[0 : height // 2, 0:width]
sliced2 = image.copy()
sliced2[height // 2 :, : width // 2] = cv2.flip(image[height // 2 :, width // 2 :], 1)
cv2.imshow("Baba isn't feel so good", sliced1)
cv2.imshow("BaaB", sliced2)

# wait until any key input
cv2.waitKey(0)
# if read key input, destroy all windows
cv2.destroyAllWindows()
