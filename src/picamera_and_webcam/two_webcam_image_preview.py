""" picamera and webcam example using opencv on Raspberri Pi to record video
"""

import cv2
import numpy as np
import imutils
from datetime import datetime
from datetime import date
import time
from time import sleep
import copy
import os
from pathlib import Path
from picamera import PiCamera
import threading

def captureImage(capId):
#     global cap0
    if capId == 0:
        ret0, frame0 = cap0.read()
        cam_number = 'cam0'
    else: 
        ret0, frame0 = cap1.read()
        cam_number = 'cam1'
    cv2.imwrite(f"{os.path.join(str(resultsPath), str(frame_number_string) + '_' + video_Name + '_' + cam_number + '.png' )}", frame0)
    return frame0, ret0
    
    
# time.sleep(20)
print(f"*** RUNNING CAMERA RECORDING PROGRAM ***")

# define file storage location
resultsPath = os.path.join(str(Path.home()), "Results", date.today().strftime("%Y%m%d"), "video")
if not os.path.exists(resultsPath):
    os.makedirs(resultsPath)

# file name generation
day = date.today()
t = time.localtime()
video_Name = day.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S",t)

global cap0
global cap1

cap0 = cv2.VideoCapture(0) # webcam
cap1 = cv2.VideoCapture(2) # webcam

if cap1.isOpened() and cap1.isOpened(): print("Could not open video device")

imageWidth = 480
imageHeight = 640

frame_rate = 60

cap0.set( cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap0.set( cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393
cap0.set( cv2.CAP_PROP_FPS, frame_rate)
cap0.set( cv2.CAP_PROP_AUTOFOCUS, 0)

cap1.set( cv2.CAP_PROP_FRAME_WIDTH, imageWidth/4) # 450 500
cap1.set( cv2.CAP_PROP_FRAME_HEIGHT, imageHeight/4) # 315 393
cap1.set( cv2.CAP_PROP_FPS, frame_rate)
cap1.set( cv2.CAP_PROP_AUTOFOCUS, 0)

# camera.start_preview(alpha=200)
frame_Number = 0 

for frame_Number in range(0,50):
    if frame_Number < 10: frame_number_string = '0' + str(frame_Number)
    else: frame_number_string = str(frame_Number)
    
    captureImage(0)
    captureImage(1)

    
cap0.release()
cap1.release()
cv2.destroyAllWindows()




