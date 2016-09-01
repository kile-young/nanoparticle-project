from PIL import Image
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from skimage.filters import sobel, threshold_adaptive, threshold_li

im = Image.open('sample2.jpg')
im = np.asarray(im)
threshold = threshold_li(im) #60
print(threshold)
im = im[:,:,0]
#cluster_im = np.zeros(im.shape)
#counts = np.zeros(255).astype(int)
pixels = np.array([])
for x in range(np.size(im, 1)):
	for y in range(np.size(im, 0)):
		val = im[y][x]
		if val>threshold:
			pixels = np.append(pixels, val)
		#counts[val]+=1
#print(counts)
pixels = pixels * float(1400)/255
print(pixels)
bins = np.linspace(1,float(1400),10)
plt.hist(pixels, bins, alpha = 0.5)
plt.show()