import cv2
print("package imported")

#read images,vedios,webcam
# img=cv2.imread("Resources/image.png")
# cv2.imshow("output",img)
# cv2.waitKey(0)

#importing vedios
cap=cv2.VideoCapture("Resources/banana.mp4")
while True:
    success ,img=cap.read()  #shows true or false
    cv2.imshow("video",img)
    if cv2.waitKey(1)&0xFF==ord('q'):#adds delay
        break #if key q is pressed it will break
