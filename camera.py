import picamera
import time

camera = picamera.PiCamera()

s='/home/pi/project/test_images/plate1.jpg'

camera.start_preview()
time.sleep(5)
camera.capture(s)

camera.close()
    
