""" Picamera example using Raspberri Pi
    
    source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4

"""

from picamera import PiCamera
from picamera import Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.resolution = (2592, 1944) # resolution maxim 2592x1944 min 64x64
camera.framerate = 15
camera.rotation = 180

camera.start_preview(alpha=200) # apha value adjust the see-though setting level from 0 to 255
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Hello world"
camera.brightness = 40 # brightness values from 0 to 100. default value 50
camera.contrast = 40
camera.image_effect = 'colorpoint'
camera.exposure_mode = 'snow'
camera.awb_mode = 'flash'
camera.annotate_text_size = 50  # size between 6 to 160. Default value 32

sleep(5)
camera.capture('/home/user/Desktop/image.jpg')
camera.stop_preview()

