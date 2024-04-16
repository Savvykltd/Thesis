import cv

import numpy as np
import matplotlib.pyplot as plt

def canny(frame):
    image_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    image_blur = cv.GaussianBlur(image_gray, (5, 5),0)
    canny = cv.Canny(image_blur, 50, 150)

def segment(frame):
    #ROI = np.array([[(0. height),(400, 300)]])\
    ROI = [((679-480)/2,(559 - 360)/2), ((679+480)/2,(559 + 360)/2)]
    cropped_img = frame[np  .min(ROI[:,1]) : np.max(ROI[:,1]),
                        np.min(ROI[:,0]) : np.max(ROI[:,0]) ]
    return cropped_img

def draw_lines(frame, lines):
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        cv.line(frame, (x1,y1), (x2,y2), [0,255,0], 2)

#Create a image reading in files in the folder

