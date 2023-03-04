import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

# ortama bulanıklaştırma
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("oratama bulanık"),plt.show()

# gaussian bulanıklaştırma
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gauss bulanık"),plt.show()

# medyan bulanıklaştırma
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("medyan bulanık"),plt.show()