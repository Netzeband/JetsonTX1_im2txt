from __future__ import division

import cv2
import Tkinter as tk
from PIL import Image as image
from PIL import ImageTk as imagetk
import tkFileDialog 
import tensorflow as tf

class CaptionWindow(object):
  def __init__(self, VideoStream, CaptionFunc = None):
    self._CaptionFunc = CaptionFunc
    self._VideoStream = VideoStream
    
    # Set up GUI
    self._Window = tk.Tk()
    self._Window.wm_title("Image Captioning Demo")
    self._Window.config(background="#FFFFFF")
    self._Window.rowconfigure(0, weight=1)
    self._Window.columnconfigure(0, weight = 1)
    self._Window.minsize(480, 320)
    
    # Graphics window
    self._ImageFrame = tk.Frame(self._Window)
    self._ImageFrame.grid(row=0, column=0, columnspan=3, rowspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    self._ImageFrame.rowconfigure(0, weight=1)
    self._ImageFrame.columnconfigure(0, weight=1)

    # Capture video frames
    self._IsVideoRunnung = True
    self._VideoLabel = tk.Label(self._ImageFrame)
    self._VideoLabel.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    self._VideoLabel.rowconfigure(0, weight=1)
    self._VideoLabel.columnconfigure(0, weight=1)
    self._showVideoFrame() 
    
    # Control Frame
    self._ControlFrame = tk.Frame(self._Window)
    self._ControlFrame.grid(row = 2, column=0, padx=10, pady=2, sticky=tk.N+tk.S)
    self._ControlFrame.rowconfigure(0, weight=0, minsize=30)
    self._ControlFrame.columnconfigure(0, weight=0)

    # Pause Button
    self._PauseButton = tk.Button(self._ControlFrame, text="Pause", command=self._pressPause)
    self._PauseButton.grid(row = 0, column = 0)
    self._Window.bind("<Key>", self._pressKey)
    
    # Captioning Button
    self._CaptionButton = tk.Button(self._ControlFrame, text="Caption", command=self._pressCaption)
    self._CaptionButton.grid(row = 0, column = 1)
    
    # Open Button
    self._OpenButton = tk.Button(self._ControlFrame, text="File...", command=self._openImage)
    self._OpenButton.grid(row = 0, column = 2)
    
    # Text Output
    self._TextFrame = tk.Frame(self._Window)
    self._TextFrame.grid(row = 3, column=0, padx=10, pady=2, sticky=tk.N+tk.S+tk.E+tk.W)
    self._TextFrame.rowconfigure(0, weight=1)
    self._TextFrame.columnconfigure(0, weight=1)
    ScrollBar = tk.Scrollbar(self._TextFrame)
    ScrollBar.grid(column=6, sticky=tk.W+tk.S+tk.N)
    self._OutputText = tk.Text(self._TextFrame, height=3, width=50)
    self._OutputText.grid(row=0, columnspan=5, column=0, sticky=tk.N+tk.S+tk.W+tk.E)
    self._OutputText.rowconfigure(0, weight=1)
    self._OutputText.columnconfigure(0, weight=1)
    ScrollBar.config(command=self._OutputText.yview)
    self._OutputText.config(yscrollcommand=ScrollBar.set)
    self._OutputText.delete('1.0', tk.END)
    self._OutputText.config(font=("Courier", 22))
    
  
  def _openImage(self):
    FileTypes = [('JPG Image Files', '*.jpg'), ('All files', '*')]
    Dialog = tkFileDialog.Open(self._ControlFrame, filetypes = FileTypes)
    FileName = Dialog.show()
    
    if not FileName == '' and not FileName == ():
      print("Open file: "+str(FileName))
      
      if self._IsVideoRunnung:
        self._pressPause()
	
      Image = image.open(FileName)
      Image = Image.resize(self._getLabelSize(self._VideoLabel, Image.width/Image.height), image.ANTIALIAS)
      Image = imagetk.PhotoImage(Image)
      self._VideoLabel.imgtk = Image
      self._VideoLabel.configure(image=Image)          
    
      self._OutputText.delete('1.0', tk.END)
  
      File = tf.gfile.GFile(FileName, "r")
      Captions = self._CaptionFunc(File.read())
        
      for i, Caption in enumerate(Captions):
        self._OutputText.insert(tk.END, str(i+1)+") "+Caption+"\n")
    
  def _showVideoFrame(self):
    if self._IsVideoRunnung:
      self._captureSingleImage()
      
    self._VideoLabel.after(1, self._showVideoFrame) 
    
    
  def _getLabelSize(self, Label, Ratio):
    LabelWidth  = max(1, Label.winfo_width()-10)
    LabelHeight = max(1, Label.winfo_height()-10)
    
    TestWidth = LabelHeight * Ratio
    
    if TestWidth <= LabelWidth:
      return (max(1, int(TestWidth)), max(1, int(LabelHeight)))
    
    TestHeight = LabelWidth / Ratio
    return (max(1, int(LabelWidth)), max(1, int(TestHeight)))
    
  def _captureSingleImage(self):
    Return, Frame = self._VideoStream.read()
    FrameImage = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGBA)
    FrameImage = cv2.resize(FrameImage, self._getLabelSize(self._VideoLabel, 480/320), interpolation = cv2.INTER_CUBIC)
    ArrayImage = image.fromarray(FrameImage)
    #ArrayImage = ArrayImage.resize(, image.ANTIALIAS)
    Image = imagetk.PhotoImage(image=ArrayImage)
    self._VideoLabel.imgtk = Image
    self._VideoLabel.configure(image=Image)
    #cv2.imencode(".jpg", Frame)
    return(cv2.imencode('.jpg', Frame)[1].tostring())
    
  def _pressPause(self):    
    self._IsVideoRunnung = not self._IsVideoRunnung
    
    if not self._IsVideoRunnung:
      self._PauseButton.config(relief=tk.SUNKEN)
      
    else:
      self._PauseButton.config(relief=tk.RAISED)

  def _pressCaption(self):
    if self._IsVideoRunnung:
      self._pressPause()
    
    self._OutputText.delete('1.0', tk.END)
  
    Image = self._captureSingleImage()
    Captions = self._CaptionFunc(Image)
        
    for i, Caption in enumerate(Captions):
      self._OutputText.insert(tk.END, str(i+1)+") "+Caption+"\n")
    
  def _pressKey(self, Event):    
    if Event.char == "p":
      print("Pressed Pause...")
      self._pressPause()
    
    if Event.char == "c":
      print("Pressed Caption...")
      self._pressCaption()
    
    if Event.char == "q":
      print("Pressed Quit...")
      self._Window.quit()
    
  def start(self):
    self._Window.mainloop()

