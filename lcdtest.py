import numpy as np
import cv2
#dimensions
height = 700
width = 1280
row_density = 4
column_density = 6

bit_height = int(height/row_density)
bit_width = int(width/column_density)
img = np.zeros((height,width,3), np.uint8)


cv2.line(img,(0,bit_height),(width,bit_height),(255,0,0),2)

cv2.line(img,(0,bit_height*2),(width,bit_height*2),(255,0,0),2)

cv2.line(img,(0,bit_height*3),(width,bit_height*3),(255,0,0),2)

cv2.line(img,(bit_width,0),(bit_width,height),(255,0,0),2)

cv2.line(img,(bit_width*2,0),(bit_width*2,height),(255,0,0),2)

cv2.line(img,(bit_width*3,0),(bit_width*3,height),(255,0,0),2)

cv2.line(img,(bit_width*4,0),(bit_width*4,height),(255,0,0),2)

cv2.line(img,(bit_width*5,0),(bit_width*5,height),(255,0,0),2)


cv2.circle(img,(bit_width/2,bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,(bit_width/2,bit_height+bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,(bit_width/2,(bit_height*2)+bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,(bit_width/2,(bit_height*3)+bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,((bit_width)+bit_width/2,bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,((bit_width*2)+bit_width/2,bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,((bit_width*3)+bit_width/2,bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,((bit_width*4)+bit_width/2,bit_height/2), 63, (0,0,255), -1)

cv2.circle(img,((bit_width*5)+bit_width/2,bit_height/2), 63, (0,0,255), -1)


while True:
    cv2.imshow('img',img)

    key = cv2.waitKey(10) % 0x100
    if key == 27: break #ESC 
