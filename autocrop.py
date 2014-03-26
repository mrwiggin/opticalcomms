'''
this splits up a raw video feed into the designated led setup, 
allowing each ledbit to be processed independently
'''
import numpy as np
import cv2
import cv2.cv as cv
import sys



if len(sys.argv) is 1:
	webcaminput = 1
else:
	webcaminput = int(sys.argv[1])
#print webcaminput

cam = cv2.VideoCapture(webcaminput)


h = 173
s = 166
v = 195

range = 50

minLineLength = 100
maxLineGap = 10
ix,iy = -1,-1
cropped = False
drawing = False # true if mouse is pressed
fx, fy = 0, 0
returnVal, uncropped = cam.read()

while True:
	returnVal,orig_frame=cam.read()
	
	height,width,d = orig_frame.shape
	
	rows,cols,ch = orig_frame.shape
	
	crop_frame = orig_frame[0:200, 0:200]
	
	print height, width
	
	frame_hsv=cv2.cvtColor(orig_frame, cv2.COLOR_BGR2HSV)
	red_lower=np.array([h-range,s-range,v-range],np.uint8)  
	red_upper=np.array([h+range,s+range,v+range],np.uint8)
	
	red=cv2.inRange(frame_hsv,red_lower,red_upper)
	ret,binary_red = cv2.threshold(red,127,255,cv2.THRESH_BINARY)
	
	contours, hierarchy = cv2.findContours(binary_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(orig_frame,contours,-1,(0,255,0),-1)
	
	#edges = cv2.Canny(binary_red,50,150,apertureSize = 3)
	
	#print contours
	#cnt = contours[0]
	#moments = cv2.moments(cnt)
	# lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	# for x1,y1,x2,y2 in lines[0]:
	#	    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
	#area = moments['m00']
	#area = cv2.contourArea(cnt)
	#x,y,w,h = cv2.boundingRect(cnt)
	#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	
	#print moments
	bit_height = (height/3)
	bit_width = (width/4)
	
	print bit_height, bit_width
	
	pt1_y, pt1_x = 252, 345
	pt2_y, pt2_x = 339, 349
	pt3_y, pt3_x = 258, 393


	# init points from input image
	pts1 = np.float32([[pt1_y,pt1_x],[pt2_y,pt2_x],[pt3_y,pt3_x]])
	#corresponding points in the output image
	pts2 = np.float32([[50,50],[600,50],[50,400]])

	M = cv2.getAffineTransform(pts1,pts2)

	orig_frame = cv2.warpAffine(orig_frame,M,(width,height))
	
	frame_gray = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2GRAY)
	ret,binary_full = cv2.threshold(frame_gray,127,255,cv2.THRESH_BINARY)
	#leftmost vertical line
	cv2.line(orig_frame,(bit_width,0),(bit_width,height),(0,0,0))
	
	#second vert line from left
	cv2.line(orig_frame,(bit_width*2,0),(bit_width*2,height),(0,0,0))
	
	cv2.line(orig_frame,(bit_width*3,0),(bit_width*3,height),(0,0,0))
	
	cv2.line(orig_frame,(0,bit_height),(width, bit_height),(0,0,0))
	
	cv2.line(orig_frame,(0,bit_height*2),(width, bit_height*2),(0,0,0))
	
	cv2.line(orig_frame,(0,bit_height*3),(width, bit_height*3),(0,0,0))
	
	#cv2.line(frame,(0,bit_height),(height, bit_width),(0,0,0))
	
	
	cv2.putText(orig_frame,'bit1',(10,500), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2)
	
	
	bit_0 = binary_full[0:bit_height, 0:bit_width]
	bit_1 = binary_full[0:bit_height, bit_width:bit_width*2]
	bit_2 = binary_full[0:bit_height, bit_width*2:bit_width*3]
	bit_3 = binary_full[0:bit_height, bit_width*3:bit_width*4]
	
	bit_4 = binary_full[bit_height:bit_height*2, 0:bit_width]
	bit_5 = binary_full[bit_height:bit_height*2, bit_width:bit_width*2]
	bit_6 = binary_full[bit_height:bit_height*2, bit_width*2:bit_width*3]
	bit_7 = binary_full[bit_height:bit_height*2, bit_width*3:bit_width*4]
	
	bit_8 = binary_full[bit_height*2:bit_height*3, 0:bit_width]
	bit_9 = binary_full[bit_height*2:bit_height*3, bit_width:bit_width*2]
	bit_10 = binary_full[bit_height*2:bit_height*3, bit_width*2:bit_width*3]
	bit_11 = binary_full[bit_height*2:bit_height*3, bit_width*3:bit_width*4]
	#bit_2 = frame[y1:y2, x1:x2]
	#bit_0 = cv2.cvtColor(bit_0, cv2.COLOR_BGR2GRAY)
	#ret,bit_0 = cv2.threshold(bit_0,127,255,cv2.THRESH_BINARY)
	
	img=cv2.GaussianBlur(orig_frame, (5,5), 0)
	#img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	#img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	#img=cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
	#cv2.line(frame, (50,50), (200,200), (0,0,0))
	#cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)
	
	offset = 600
	#cv2.imshow('red',red)
	
	
	cv2.imshow('img',orig_frame)
	cv2.imshow('bit0',bit_0)
	cv.MoveWindow('bit0',offset,0)
	cv2.imshow('bit1',bit_1)
	cv.MoveWindow('bit1',offset+bit_width,0)
	
	cv2.imshow('bit2',bit_2)
	cv.MoveWindow('bit2',offset+bit_width*2,0)
	
	cv2.imshow('bit3',bit_3)
	cv.MoveWindow('bit3',offset+bit_width*3,0)
	
	cv2.imshow('bit4',bit_4)
	cv.MoveWindow('bit4',offset,bit_height)
	
	cv2.imshow('bit5',bit_5)
	cv.MoveWindow('bit5',offset+bit_width,bit_height)
	
	cv2.imshow('bit6',bit_6)
	cv.MoveWindow('bit6',offset+bit_width*2,bit_height)
	
	cv2.imshow('bit7',bit_7)
	cv.MoveWindow('bit7',offset+bit_width*3,bit_height)
	
	cv2.imshow('bit8',bit_8)
	cv.MoveWindow('bit8',offset,bit_height*2)
	
	cv2.imshow('bit9',bit_9)
	cv.MoveWindow('bit9',offset+bit_width,bit_height*2)
	
	cv2.imshow('bit10',bit_10)
	cv.MoveWindow('bit10',offset+bit_width*2,bit_height*2)
	
	cv2.imshow('bit11',bit_11)
	cv.MoveWindow('bit11',offset+bit_width*3,bit_height*2)
	
	
	key = cv2.waitKey(10) % 0x100
	if key == 27: break #ESC 