""" Webcam image capture example using Raspberri Pi
"""

import cv2
import numpy as np
import imutils
from datetime import datetime
from datetime import date
import time
import copy
import os
from pathlib import Path

def captureImage():
    global cap0 
    ret0, frame0 = cap0.read()
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
#    frame1r = imutils.resize(frame1, width=frame0.shape[1], height=frame1.shape[0])
#    concat0 = cv2.hconcat([frame0, frame1r])
#    concat1 = cv2.hconcat([concat0, frame2])
#     return frame0, frame1, frame2, ret0, ret1, ret2
    return frame0, ret0


# time.sleep(20)
print(f"*** RUNNING CAMERA RECORDING IMAGE PROGRAM ***")

# define file storage location
resultsPath = os.path.join(str(Path.home()), "Results", date.today().strftime("%Y%m%d"), "video")
if not os.path.exists(resultsPath):
    os.makedirs(resultsPath)

# file name generation
day = date.today()
t = time.localtime()
videoName = day.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S",t)

cap0 = cv2.VideoCapture(1)

if not (cap0.isOpened()): print("Could not open video device")

imageWidth = 480
imageHeight = 640
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393

frame0, ret0 = captureImage()
cv2.imshow('camera0', frame0)
cv2.imwrite(f"{os.path.join(str(resultsPath), videoName + 'cam0.jpg' )}", frame0)

cv2.destroyAllWindows()



