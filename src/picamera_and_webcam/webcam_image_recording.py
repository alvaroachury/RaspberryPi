""" picamera and webcam example using opencv on Raspberri Pi to record video
    
"""

import cv2
import numpy as np
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

def getPiCameraImage( resultsPath, frame_Number, video_Name):
    camera.capture(f"{os.path.join(str(resultsPath), str(frame_Number) + '_' + video_Name + '_cam0.png' )}")
    
   
    
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

cap1 = cv2.VideoCapture(1) # webcam

if cap1.isOpened(): print("Could not open video device")

imageWidth = 480 #480
imageHeight = 640 #640
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393
cap1.set(cv2.CAP_PROP_FPS,5)
cap1.set(cv2.CAP_PROP_AUTOFOCUS, 0)


# camera.start_preview(alpha=200)
frame_Number = 0 
print('..>', resultsPath)
for frame_Number in range(0,10):
    frame1, ret1 = captureImage(cap1)
    
for frame_Number in range(0,50):
    if frame_Number < 10: frame_number_string = '0' + str(frame_Number)
    else: frame_number_string = str(frame_Number)
    frame1, ret1 = captureImage(cap1)
    if ret1:
        cv2.imwrite(f"{os.path.join(str(resultsPath), str(frame_number_string) + '_' + video_Name + '_cam1.png' )}", frame1)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
    
cap1.release()
# cap1.close()
# cv2.destroyAllWindows()





