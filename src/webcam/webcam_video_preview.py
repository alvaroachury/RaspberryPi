""" Webcam example using opencv on Raspberri Pi to record video
    
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

cap0 = cv2.VideoCapture(1)


print(f"CAM0: {cap0} ") # CAM0: < cv2.VideoCapture 0xea82b910> , CAM1: < cv2.VideoCapture 0xea82b900> , CAM0: < cv2.VideoCapture 0xea82b910>

if not (cap0.isOpened()): print("Could not open video device")

imageWidth = 480
imageHeight = 640
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, imageWidth) # 450 500
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, imageHeight) # 315 393

frame0, ret0 = captureImage()

print(f"{os.path.join(str(resultsPath), videoName + 'cam0.avi' )}")
outVideo0 = cv2.VideoWriter(f"{os.path.join(str(resultsPath), videoName + 'cam0.avi' )}", cv2.VideoWriter_fourcc(*'XVID'), 20, (imageHeight, imageWidth) )

while True:
    frame0, ret0 = captureImage()
    if ret0 :
        
        outVideo0.write(frame0)
        
        cv2.imshow('camera0', frame0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap0.release()
outVideo0.release()
cv2.destroyAllWindows()



