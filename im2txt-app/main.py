import cv2
import CaptionWindow
import Im2TextModel
import os

# Options
Scriptpath     = os.path.dirname(os.path.realpath(__file__))
StreamOptions  = "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420, framerate=(fraction)24/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
VocabularyPath = os.path.join(Scriptpath, "..", "im2txt-model", "pre-trained", "word_counts.txt")
ModelPath      = os.path.join(Scriptpath, "..", "im2txt-model", "pre-trained", "model.ckpt-2000000")

VideoStream = cv2.VideoCapture(StreamOptions)

Im2Text = Im2TextModel.Im2Text(ModelPath, VocabularyPath)
#Im2Text = Im2TextModel.DummyModel(ModelPath, VocabularyPath)
Window = CaptionWindow.CaptionWindow(VideoStream, Im2Text.createCaptions)

Window.start()

print("Close all devices...")

VideoStream.release()
cv2.destroyAllWindows() 
