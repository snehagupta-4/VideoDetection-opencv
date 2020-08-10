import cv2 as cv
import numpy as np


def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar("lh", "Tracking", 0, 255, nothing)
cv.createTrackbar("ls", "Tracking", 0, 255, nothing)
cv.createTrackbar("lv", "Tracking", 0, 255, nothing)
cv.createTrackbar("uh", "Tracking", 255, 255, nothing)
cv.createTrackbar("us", "Tracking", 255, 255, nothing)
cv.createTrackbar("uv", "Tracking", 255, 255, nothing)

while (True):
    frame = cv.imread('lena.jpg')
    frame = cv.resize(frame, (512, 512))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    l_h=cv.getTrackbarPos("lh", "Tracking")
    l_s = cv.getTrackbarPos("ls", "Tracking")
    l_v = cv.getTrackbarPos("lv", "Tracking")
    u_h = cv.getTrackbarPos("uh", "Tracking")
    u_s = cv.getTrackbarPos("us", "Tracking")
    u_v = cv.getTrackbarPos("uv", "Tracking")

    lb = np.array([l_h, l_s, l_v])
    ub = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, lb, ub)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key = cv.waitKey(1)
    if key == 27:
        break


cv.destroyAllWindows()

