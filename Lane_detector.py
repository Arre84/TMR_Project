import cv2
import matplotlib.pyplot as plt
import numpy as np

#----------------------------------------------------

def load_image(img):
    cv2.imread(img)
    return cv2.imread(img)

def preprocessing(img):
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grey,(5,5),0)
    edged_image = cv2.Canny(blurred,100,230)
    return edged_image


prueba = load_image("Prueba2.jpg")
image = preprocessing(prueba)
cv2.imshow("Test",image)
cv2.waitKey(0)
cv2.destroyAllWindows()