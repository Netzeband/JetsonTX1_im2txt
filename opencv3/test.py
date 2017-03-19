import numpy as np
import cv2

cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)360,format=(string)I420, framerate=(fraction)24/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Display the resulting frame
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 
