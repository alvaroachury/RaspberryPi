cam0='python3 /home/user/Documents/Repo/RaspberryPi/src/picamera_and_webcam/picamera_image_recording.py'
cam1='python3 /home/user/Documents/Repo/RaspberryPi/src/picamera_and_webcam/webcam_image_recording.py'
taskset -c 0,1,2 $cam0 -c & taskset -c 3 $cam1
