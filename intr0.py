import cv2
print("package imported")
#read images,vedios,webcam
img=cv2.imread("Resources/image.png")
cv2.imshow("output",img)
cv2.waitKey(0)