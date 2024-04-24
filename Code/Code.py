import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def canny(frame):
    image_gray =  cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(image_gray,(5,5),0)
    
    # Parameters for Canny Edge Detection
    low_threshold = 100   # The minimum value for the hysteresis threshold:
                        # any edge with a weight lower than this value will be discarded.
    high_threshold = 300  # The maximum value for the hysteresis threshold. An edge is considered strong if the weight of all the pixels in the nx
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
cap = cv.VideoCapture("project_video.mp4")

while(True):
    ret, frame = cap.read()
    
    # if not ret:
    #     print("end of video file...")
    #     break
    canny(frame)
    cropped_img = segment(frame)
    gray = cv.cvtColor(cropped_img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150)
    lines = cv.HoughLinesP(edges, cv.HOUGH_PROBABILISTIC, dp=18, minLineLength=40, maxLineGap=50)
    draw_lines(frame, lines)
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    cv.destroyAllWindows()




