""" Picamera example using Raspberri Pi to record video
    
    source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6

"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview(alpha=200) # apha value adjust the see-though setting level from 0 to 255
camera.resolution = (64, 64) # maxim resolution 1920x1080
camera.start_recording('/home/user/Desktop/video0.h264')
#camera.framerate = 15
sleep(5)
camera.stop_recording()
camera.stop_preview()