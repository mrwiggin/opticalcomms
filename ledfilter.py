import cv2
import cv2.cv as cv
import sys
import numpy as np

if len(sys.argv) is 1:
	webcaminput = 1
else:
	webcaminput = int(sys.argv[1])
#print webcaminput

def nothing(x):
    pass


capture = cv2.VideoCapture(webcaminput)

cv2.namedWindow('sliders')
cv2.createTrackbar('Hue','sliders',0,255,nothing)
cv2.createTrackbar('Saturation','sliders',0,255,nothing)
cv2.createTrackbar('Value','sliders',0,255,nothing)
cv2.createTrackbar('Range','sliders',0,100,nothing)

cv2.createTrackbar('thresh','sliders',0,255,nothing)
cv2.createTrackbar('max','sliders',0,255,nothing)

preset_h = 100
preset_s = 150
preset_v = 80

preset_thresh = 127
preset_max = 255

#set trackbars to presets
cv2.setTrackbarPos('Hue','sliders',100)
cv2.setTrackbarPos('Saturation','sliders',150)
cv2.setTrackbarPos('Value','sliders',80)

cv2.setTrackbarPos('thresh','sliders',127)
cv2.setTrackbarPos('max','sliders',255)

range = 50
cv2.setTrackbarPos('Range','sliders',range)

while True:
	returnVal, raw_frame = capture.read()
	height,width,d = raw_frame.shape
	
	
	h = cv2.getTrackbarPos('Hue','sliders')
	s = cv2.getTrackbarPos('Saturation','sliders')
	v = cv2.getTrackbarPos('Value','sliders')
	range = cv2.getTrackbarPos('Range','sliders')
	
	thresh = cv2.getTrackbarPos('thresh','sliders')
	max = cv2.getTrackbarPos('max','sliders')
	
	hsv_frame=cv2.cvtColor(raw_frame, cv2.COLOR_BGR2HSV)
	
	hsv_lower=np.array([h-range,s-range,v-range],np.uint8)
	hsv_upper=np.array([h+range,s+range,v+range],np.uint8)
	
	hsv=cv2.inRange(hsv_frame,hsv_lower,hsv_upper)
	
	frame_gray = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2GRAY)
	ret,binary_full = cv2.threshold(frame_gray,thresh,max,cv2.THRESH_BINARY)
	
	cv2.imshow('bin', binary_full)
	cv2.imshow('hsv',hsv)
	cv.MoveWindow('bin',300,0)
	key = cv2.waitKey(10) % 0x100
	if key == 27: break #ESC 