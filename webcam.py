import cv2

camera = cv2.VideoCapture(0)
i = 0
while i < 2:
    raw_input('Press Enter to capture')
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
    i=i+1
del(camera)
