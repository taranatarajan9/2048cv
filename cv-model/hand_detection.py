import cv2 as cv
import numpy as np
import imutils
from logic.directions import Direction

def capture_video():
    cam = cv.VideoCapture(0) # accesses webcam
    ret = True
    first_frame = cv.CreateImage((10,10),8,3)
    first = True
    while ret:
        ret, frame = cam.read() # saves the frame & whether a frame was opened
        if first:
            first = False
            first_frame = frame

        frame = imutils.resize(frame, width=500)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (21,21), 0)

        delta = cv.absdiff(first_frame, gray)
        thresh = cv.threshold(delta, 25, 255, cv.THRESH_BINARY)
        thresh = cv.dilate(thresh, None, iterations = 2)

        contours = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)



    return direction
