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

   
# time.sleep(20)
print(f"*** RUNNING PI CAMERA RECORDING PROGRAM ***")

# define file storage location
resultsPath = os.path.join(str(Path.home()), "Results", date.today().strftime("%Y%m%d"), "video")
if not os.path.exists(resultsPath):
    os.makedirs(resultsPath)

# file name generation
day = date.today()
t = time.localtime()
video_Name = day.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S",t)

camera = PiCamera() # picamera

imageWidth = 480
imageHeight = 640
camera.resolution = (480, 640) # maxim resolution 1920x1080
camera.framerate = 60

# camera.start_preview(alpha=200)
frame_Number = 0 
print('..>', resultsPath)
for frame_Number in range(0,50):
    if frame_Number < 10: frame_number_string = '0' + str(frame_Number)
    else: frame_number_string = str(frame_Number)
    
    camera.capture(f"{os.path.join(str(resultsPath), str(frame_number_string) + '_' + video_Name + '_cam0.png' )}")
        
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
    
#     frame_Number = frame_Number + 1
    
camera.stop_preview()
camera.close()
# cv2.destroyAllWindows()





