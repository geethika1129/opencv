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
img = cv2.imread("Resources/image.png")
kernel=np.ones((5,5),np.uint8)
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggrey,(7,7),0)
imgcanny=cv2.Canny(img,150,200)
imgdil=cv2.dilate(imgcanny,kernel,iterations=1)
imgeroded=cv2.erode(imgdil,kernel,iterations=1)
cv2.imshow( "Gray Image",imggrey)
cv2.imshow( "Gray Image",imgblur)
cv2.imshow( "Gray Image",imgcanny)
cv2.imshow( "Gray Image",imgdil)
cv2.imshow( "Gray Image",imgeroded)
cv2.waitKey(0)