from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from identify_face_image import identify_function
import cv2
import time
import os
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

check, frame = webcam.read()
#time.sleep(5)
print(check) #prints true as long as the webcam is running
print(frame) #prints matrix values of each framecd
cv2.imshow("Capturing", frame)
key = cv2.waitKey(1)
cv2.imwrite(filename='test_img/test.jpg', img=frame)
webcam.release()
cv2.waitKey(1650)
cv2.destroyAllWindows()
identify_function()
os.remove('test_img/test.jpg')
