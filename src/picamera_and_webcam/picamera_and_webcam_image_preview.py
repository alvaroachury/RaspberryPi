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
    ret0, frame0 = capId.read()
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

camera = PiCamera() # picamera
cap1 = cv2.VideoCapture(1) # webcam

if cap1.isOpened(): print("Could not open video device")

imageWidth = 240
imageHeight = 320
camera.resolution = (480, 640) # maxim resolution 1920x1080
camera.framerate = 30
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393

# camera.start_preview(alpha=200)
frame_Number = 0 

for frame_Number in range(0,20):
    if frame_Number < 10: frame_number_string = '0' + str(frame_Number)
    else: frame_number_string = str(frame_Number)
    
    camera.capture(f"{os.path.join(str(resultsPath), str(frame_number_string) + '_' + video_Name + '_cam0.png' )}")
    frame1, ret1 = captureImage(cap1)
    cv2.imwrite(f"{os.path.join(str(resultsPath), str(frame_number_string) + '_' + video_Name + '_cam1.png' )}", frame1)

    
camera.stop_preview()
camera.close()
cap1.release()
cv2.destroyAllWindows()




