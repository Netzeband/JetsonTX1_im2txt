#########################################################################
# License Agreement
# For Open Source Computer Vision Library
# (3-clause BSD License)
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions 
# are met:
#
#    Redistributions of source code must retain the above copyright 
#    notice, this list of conditions and the following disclaimer.
#    Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in 
#    the documentation and/or other materials provided with the 
#    distribution.
#    Neither the names of the copyright holders nor the names of the 
#    contributors may be used to endorse or promote products derived 
#    from this software without specific prior written permission.
#
# This software is provided by the copyright holders and contributors 
# “as is” and any express or implied warranties, including, but not 
# limited to, the implied warranties of merchantability and fitness 
# for a particular purpose are disclaimed. In no event shall copyright 
# holders or contributors be liable for any direct, indirect, incidental, 
# special, exemplary, or consequential damages (including, but not 
# limited to, procurement of substitute goods or services; loss of 
# use, data, or profits; or business interruption) however caused and 
# on any theory of liability, whether in contract, strict liability, 
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such 
# damage.
#########################################################################

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
