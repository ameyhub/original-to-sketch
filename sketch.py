import cv2
import matplotlib.pyplot as plt

#img = cv2.imread('asd.png') 
image = plt.imread('asd.png') #chanage the Image name 
plt.imshow(image)
plt.show()

#gray scale
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(image)
plt.show()

#invert
img_invert = cv2.bitwise_not(image)
plt.imshow(img_invert)
plt.show()

#blur
image_blur = cv2.GaussianBlur(img_invert,(21,21), sigmaX=0, sigmaY=0)
plt.imshow(image_blur)
plt.show()


#fuction to make a sketch
def get(x,y):
    return cv2.divide(x, 255-y, scale=256)

final = get(image, image_blur)

plt.imshow(final)
plt.show()