import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)

camera = picamera.PiCamera()

s='/home/pi/project/test_images/abc.jpg'

    
trig=18
echo=23
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trig,0)
time.sleep(1)
GPIO.output(trig,1)
time.sleep(0.00001)
GPIO.output(trig,0)
while GPIO.input(echo)==0:
    st=time.time()
while GPIO.input(echo)==1:
    et=time.time()
t=et-st
d=t*17150
DISTANCE=d-0.5
if d>20 and d<200:
    print 'Distance is ',DISTANCE,' cm'
        
    camera.start_preview()
    time.sleep(2)
    camera.capture(s)
    camera.close()

else:
    print 'out of range'
    
