import cv2
import numpy

def grayscale(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray_image

def threshold(image):
    ret,img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    return img
