import cv2
import numpy as np
print("package imported")

#read images,vedios,webcam
# img=cv2.imread("Resources/image.png")
# cv2.imshow("output",img)
# cv2.waitKey(0)

#importing vedios
# cap=cv2.VideoCapture("Resources/banana.mp4")
# #if video cam mention id //we can mention the sizes
# while True:
#     success ,img=cap.read()  #shows true or false
#     cv2.imshow("video",img)
#     if cv2.waitKey(1)&0xFF==ord('q'):#adds delay
#         break #if key q is pressed it will break

#using the external webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
#
# while True:
#     success ,img=cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):#adds delay
#        break #if key q is pressed it will break
#functions
#basic functions
# img = cv2.imread("Resources/image.png")
# kernel=np.ones((5,5),np.uint8)
# imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imggrey,(7,7),0)
# imgcanny=cv2.Canny(img,150,200)
# imgdil=cv2.dilate(imgcanny,kernel,iterations=1)
# imgeroded=cv2.erode(imgdil,kernel,iterations=1)
# cv2.imshow( "Gray Image",imggrey)
# cv2.imshow( "Gray Image",imgblur)
# cv2.imshow( "Gray Image",imgcanny)
# cv2.imshow( "Gray Image",imgdil)
# cv2.imshow( "Gray Image",imgeroded)
# cv2.waitKey(0)

#reshape,size of image
# img=cv2.imread("Resources/image.png")
# print(img.shape)
# imgresize=cv2.resize(img,(300,200))
# imgcrop=img[0:200,200:500]
# #cv2.imshow("output",img)
# cv2.imshow("output",imgcrop)
# cv2.waitKey(0)

# img=np.zeros((512,512,3),np.uint8)
# print(img.shape)
#img[:]=255,0,0 #colors entire blue
# cv2.imshow("output",img)
# cv2.waitKey(0)

#creating lines
# cv2.line(img,(0,0),(300,300),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),3) #rectangle will be filled with red cv2.FILLED in last arg
# cv2.circle(img,(400,50),30,(255,255,0),5)
# cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,15))
# cv2.imshow("output",img)
# cv2.waitKey(0)

#flatten images refer pic😒

#joining images
# img=cv2.imread('Reasources/image.png')
#
# imghor=np.hstack((img,img))
# imgver=np.vstack((img,img))
# cv2.imshow("hor",imghor)
# cv2.imshow("output",imgver)
#cv2.waitKey(0)

#detect color
# img=cv2.imread('Resources/image.png')
# imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("output",imghsv)
# cv2.waitKey(0)

#face detection
facecascade=cv2.CascadeClassifier()
img=cv2.imread('Resources/')