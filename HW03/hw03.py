import numpy as np
import matplotlib.pyplot as plt
import cv2
import math as mt

img = cv2.imread('B.jpg',0)
print(f"Image size is {img.shape}")
U, S, V = np.linalg.svd(img)
print(f"U shape is {U.shape}, S shape is {S.shape}, S shape is {V.shape}")

s = min(img.shape)
val = [1, 0.8, 0.5, 0.2, 0.1, 0.05]
nSingular = [mt.floor(s * val[i]) for i in range(len(val))]
print(nSingular)
plt.figure(figsize=[9.6, 7])
for i in range(6):
    low_rank = U[:, :nSingular[i]] @ np.diag(S[:nSingular[i]]) @ V[:nSingular[i], :]
    plt.subplot(2,3,i+1), plt.imshow(low_rank, cmap = 'gray')
    plt.axis('off'), plt.title(f"Image with {val[i]*100}% Singulars({nSingular[i]})", fontsize=10)
plt.show()