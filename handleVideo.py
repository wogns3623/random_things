import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("starting video capture")
check = True
while True:
    if check:
        print(
            capture.get(cv2.CAP_PROP_FPS),
            capture.get(cv2.CAP_PROP_BRIGHTNESS),
            sep="\n"
        )
        check = False
    # frame is image of current frame
    # ret is boolean of getting frame success
    ret, frame = capture.read()
    cv2.imshow("videoFrame", frame)
    # check key input in 1ms delay
    # if delay is 0, frame doesn't update
    key = cv2.waitKey(1)
    print(f"brightness is {capture.get(cv2.CAP_PROP_BRIGHTNESS)}")
    print(f"contrast is {capture.get(cv2.CAP_PROP_CONTRAST)}")
    print(f"saturation is {capture.get(cv2.CAP_PROP_SATURATION)}")
    print(f"hue is {capture.get(cv2.CAP_PROP_HUE)}")
    print(f"gain is {capture.get(cv2.CAP_PROP_GAIN)}")
    print(f"exposure is {capture.get(cv2.CAP_PROP_EXPOSURE)}")
    if key == ord("w"):
        curBrightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
        capture.set(cv2.CAP_PROP_BRIGHTNESS, curBrightness + 1)
    elif key == ord("s"):
        curBrightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
        capture.set(cv2.CAP_PROP_BRIGHTNESS, curBrightness - 1)
    elif key > 0:
        print("end video capture")
        capture.release()
        cv2.destroyWindow("videoFrame")
        break
