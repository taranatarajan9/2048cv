import cv2 as cv
import numpy as np
from logic.directions import Direction

def capture_video():
    cam = cv.VideoCapture(0) # accesses webcam
    ret = True
    while ret:
        ret, frame = cam.read()

        

    return direction
