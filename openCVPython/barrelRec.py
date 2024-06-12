import argparse
from cmath import rect

import numpy as np
import cv2 as cv


# max_value = 255
#
# low_b = 0
# low_g = 0
# low_r = 0
#
# high_b = max_value
# high_g = max_value
# high_r = max_value
# hsvWindow = 'Object Detection HSV'
# rgbPassWindow = 'RGB Filter Pass'
#
# low_b_name = 'Low B'
# low_g_name = 'Low G'
# low_r_name = 'Low R'
# high_B_name = 'High B'
# high_G_name = 'High g'
# high_R_name = 'High R'
#
# max_value_H = 360 // 2
# low_H = 0
# low_S = 0
# low_V = 0
#
# high_H = max_value_H
# high_S = max_value
# high_V = max_value
#
# low_H_name = 'Low H'
# low_S_name = 'Low S'
# low_V_name = 'Low V'
#
# high_H_name = 'High H'
# high_S_name = 'High S'
# high_V_name = 'High V'
#
#
# def on_low_H_thresh_trackbar(val):
#     global low_H
#     global high_H
#     low_H = val
#     low_H = min(high_H - 1, low_H)
#     cv.setTrackbarPos(low_H_name, hsvWindow, low_H)
#
#
# def on_high_H_thresh_trackbar(val):
#     global low_H
#     global high_H
#     high_H = val
#     high_H = max(high_H, low_H + 1)
#     cv.setTrackbarPos(high_H_name, hsvWindow, high_H)
#
#
# def on_low_S_thresh_trackbar(val):
#     global low_S
#     global high_S
#     low_S = val
#     low_S = min(high_S - 1, low_S)
#     cv.setTrackbarPos(low_S_name, hsvWindow, low_S)
#
#
# def on_high_S_thresh_trackbar(val):
#     global low_S
#     global high_S
#     high_S = val
#     high_S = max(high_S, low_S + 1)
#     cv.setTrackbarPos(high_S_name, hsvWindow, high_S)
#
#
# def on_low_V_thresh_trackbar(val):
#     global low_V
#     global high_V
#     low_V = val
#     low_V = min(high_V - 1, low_V)
#     cv.setTrackbarPos(low_V_name, hsvWindow, low_V)
#
#
# def on_high_V_thresh_trackbar(val):
#     global low_V
#     global high_V
#     high_V = val
#     high_V = max(high_V, low_V + 1)
#     cv.setTrackbarPos(high_V_name, hsvWindow, high_V)
#
#
# def on_low_B_thresh_trackbar(val):
#     global low_b
#     global high_b
#     low_b = val
#     low_b = min(high_b - 1, low_b)
#     cv.setTrackbarPos(low_b_name, rgbPassWindow, low_b)
#
#
# def on_high_B_thresh_trackbar(val):
#     global low_b
#     global high_b
#     high_b = val
#     high_b = max(high_b, low_b + 1)
#     cv.setTrackbarPos(high_B_name, rgbPassWindow, high_b)
#
#
# def on_low_G_thresh_trackbar(val):
#     global low_g
#     global high_g
#     low_g = val
#     low_g = min(high_g - 1, low_g)
#     cv.setTrackbarPos(low_g_name, rgbPassWindow, low_g)
#
#
# def on_high_G_thresh_trackbar(val):
#     global low_g
#     global high_g
#     high_g = val
#     high_g = max(high_g, low_g + 1)
#     cv.setTrackbarPos(high_G_name, rgbPassWindow, high_g)
#
#
# def on_low_R_thresh_trackbar(val):
#     global low_r
#     global high_r
#     low_r = val
#     low_r = min(high_r - 1, low_r)
#     cv.setTrackbarPos(low_r_name, rgbPassWindow, low_r)
#
#
# def on_high_R_thresh_trackbar(val):
#     global low_r
#     global high_r
#     high_r = val
#     high_r = max(high_r, low_r + 1)
#     cv.setTrackbarPos(high_R_name, rgbPassWindow, high_r)
#
#
# cv.namedWindow("Object Detection HSV")
# cv.createTrackbar(low_H_name, hsvWindow, low_H, max_value_H, on_low_H_thresh_trackbar)
# cv.createTrackbar(high_H_name, hsvWindow, high_H, max_value_H, on_high_H_thresh_trackbar)
# cv.createTrackbar(low_S_name, hsvWindow, low_S, max_value, on_low_S_thresh_trackbar)
# cv.createTrackbar(high_S_name, hsvWindow, high_S, max_value, on_high_S_thresh_trackbar)
# cv.createTrackbar(low_V_name, hsvWindow, low_V, max_value, on_low_V_thresh_trackbar)
# cv.createTrackbar(high_V_name, hsvWindow, high_V, max_value, on_high_V_thresh_trackbar)
#
# cv.namedWindow("RGB Filter Pass")
# cv.createTrackbar(low_b_name, rgbPassWindow, low_b, max_value, on_low_B_thresh_trackbar)
# cv.createTrackbar(high_B_name, rgbPassWindow, high_b, max_value, on_high_B_thresh_trackbar)
# cv.createTrackbar(low_g_name, rgbPassWindow, low_g, max_value, on_low_G_thresh_trackbar)
# cv.createTrackbar(high_G_name, rgbPassWindow, high_g, max_value, on_high_G_thresh_trackbar)
# cv.createTrackbar(low_r_name, rgbPassWindow, low_r, max_value, on_low_R_thresh_trackbar)
# cv.createTrackbar(high_R_name, rgbPassWindow, high_r, max_value, on_high_R_thresh_trackbar)

while True:
    cap = cv.VideoCapture("Resources/BarrelVideo.mp4")

    if not cap.isOpened():
        print("Cannot open video")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow('frame', frame)

        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        low_H = 0
        high_H = 20

        low_S = 172
        high_S= 255

        low_V = 59
        high_V=202
        frame_thresholdHSV = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

        cv.imshow("HSVFilter", frame_thresholdHSV)

        smootherFrame = cv.medianBlur(frame_thresholdHSV, 5)
        imgResult = cv.bitwise_and(frame, frame, mask=smootherFrame)

        cv.imshow("Smooth + ReColor", imgResult)

        low_b = 2
        high_b = 255
        low_g = 0
        high_g = 255
        low_r = 0
        high_r = 206

        frame_thresholdRGB = cv.inRange(imgResult, (low_b, low_g, low_r), (high_b, high_g, high_r))

        erSize = 2;
        element = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2 * erSize + 1, 2 * erSize + 1),(erSize, erSize))

        eroded = cv.erode(frame_thresholdRGB, element )
        cv.imshow("Cleaning", eroded)

        # greenFilter = cv.cvtColor(imgResult, cv.COLOR_BGR2)

        smoothFrame2 = cv.medianBlur(eroded, 3)
        allEffectFinal = cv.bitwise_and(frame, frame, mask=smoothFrame2)

        cv.imshow("Final ", allEffectFinal)

        grayFilter = cv.cvtColor(allEffectFinal, cv.COLOR_BGR2GRAY)
        cv.imshow("Grey Step", grayFilter)
        grayVals = np.float32(grayFilter)
        # corners = cv.goodFeaturesToTrack(grayFilter,25,.01,10,10)
        # corners = np.int0(corners)
        # xP, yP = -1, -1
        # for i in corners:
        #     x,y = i.ravel();
        #     cv.circle(frame,(x,y),3,255,-1)
        #     # if not xP == -1:
        #     #     cv.line(frame, (x,y), (xP,yP), (0,0,255), thickness=3, lineType=8)
        #     # xP, yP = x, y;
        # cv.imshow('frame', frame)
        #
        #
        # dst = cv.cornerHarris(grayVals, 5, 7, 0.0001)
        # dst = cv.dilate(dst, None)
        # frame[dst > 0.01 * dst.max()] = [0, 0, 255]
        # cv.imshow('dst', frame)
        #
        # sift = cv.SIFT_create()
        # kp = sift.detect(grayFilter, None)
        # img = cv.drawKeypoints(grayFilter, kp, frame)
        # cv.imshow('sift_keypoints.jpg', frame)

        ret, binary = cv.threshold(grayFilter, 20, 255,
                                    cv.THRESH_BINARY)
        # Display the binary image
        cv.imshow('Binary image', binary)


        # Find the contours on the inverted binary image, and store them in a list
        # Contours are drawn around white blobs.
        # hierarchy variable contains info on the relationship between the contours
        contours, hierarchy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

        # Draw the contours (in red) on the original image and display the result
        # Input color code is in BGR (blue, green, red) format
        # -1 means to draw all contours
        with_contours = cv.drawContours(frame, contours, -1, (255, 0, 255), 3)
        cv.imshow('Detected contours', with_contours)

        # Show the total number of contours that were detected
        print('Total number of contours detected: ' + str(len(contours)))


        # x is the starting x coordinate of the bounding box
        # y is the starting y coordinate of the bounding box
        # w is the width of the bounding box
        # h is the height of the bounding box
        # Draw a bounding box around all contours
        for i in range(0,len(contours)):
            rect = cv.minAreaRect(contours[i])
            print("area: " + str(cv.contourArea(contours[i])))
            if  cv.contourArea(contours[i]) < 10 and cv.contourArea(contours[i]) >0 :
                box = cv.boxPoints(rect)
                box = np.int0(box)

                cv.drawContours(frame, [box], 0, (0, 255,0 ), 2)
                cv.minAreaRect(with_contours, (x, y), (x + w, y + h), (255, 0, 0), 5)

        cv.imshow('Bounded', frame)


        if cv.waitKey(25) == ord('q'):
            exit()
cap.release()
cv.destroyAllWindows()
