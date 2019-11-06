from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import qdarkstyle
import cv2
import math
import numpy as np


img = cv2.imread('/Users/YoChen/Documents/GitHub/Img-Processing/HW04/test.jpg',0)
cv2.imshow('a',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("joj")