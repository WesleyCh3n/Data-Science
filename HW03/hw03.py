import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import math as mt

img = cv2.imread('/Users/YoChen/Documents/GitHub/Img-Processing/HW04/test.jpg',0)
print(img.shape)
U, S, V = np.linalg.svd(img)
print(a.shape)
print(b.shape)
print(c.shape)