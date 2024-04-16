import cv

import numpy as np
import matplotlib.pyplot as plt

def canny(frame):
    image_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    image_blur = cv.GaussianBlur(image_gray, (5, 5),0)
    canny = cv.Canny(image_blur, 50, 150)

def segment(frame):
    ROI = np.array([[(0. height),(400, 300)]])
