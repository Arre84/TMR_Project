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
    withe_color = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
    edged_image = cv2.Canny(withe_color,150,255)
    return edged_image


prueba = load_image("Prueba1.png")
image = preprocessing(prueba)
cv2.imshow("Test",image)
cv2.waitKey(0)
cv2.destroyAllWindows()