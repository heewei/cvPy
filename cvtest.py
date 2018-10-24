import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('B1Lancer.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('look', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
