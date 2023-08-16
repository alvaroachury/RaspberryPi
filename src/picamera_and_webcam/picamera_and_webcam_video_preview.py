""" picamera and webcam example using opencv on Raspberri Pi to record video
    
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
from picamera import PiCamera


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
videoName = day.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S",t)

camera = PiCamera() # picamera
cap1 = cv2.VideoCapture(1) # webcam

if cap1.isOpened(): print("Could not open video device")

imageWidth = 480
imageHeight = 640
camera.resolution = (640, 480) # maxim resolution 1920x1080
camera.framerate = 30
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393

camera.start_preview()
camera.start_recording(f"{os.path.join(str(resultsPath), videoName + 'cam0.h264' )}")

outVideo1 = cv2.VideoWriter(f"{os.path.join(str(resultsPath), videoName + 'cam1.avi' )}", cv2.VideoWriter_fourcc(*'XVID'), 30, (imageHeight, imageWidth) )

while True:
    frame1, ret1 = captureImage(cap1)
    
    if ret1:
        outVideo1.write(frame1)
        cv2.imshow('camera1', frame1)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.stop_recording()
camera.stop_preview()
cap1.release()
outVideo1.release()
cv2.destroyAllWindows()




