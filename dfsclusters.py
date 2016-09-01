from PIL import Image
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from skimage.filters import sobel, threshold_adaptive, threshold_li
#im = Image.open('sample1.jpg')
#im = Image.open('sample2.jpg')
im = Image.open('sample2.jpg')
im = np.asarray(im)
threshold = threshold_li(im) #60
print(threshold)
im = im[:,:,0]
sobel_edges = sobel(im)
cluster_im = np.zeros(im.shape)
thresholds = threshold_adaptive(im, 101, method = 'mean')
def dfs(im, x, y):
	stack = [(x,y)]
	clustertotal, numpixels = int(im[y][x]),1
	while stack != []:
		x, y = stack.pop()
		neighbors = [(x+1, y), (x, y+1), (x+1, y+1)]
		for neighbor in neighbors:
			x,y = neighbor[0], neighbor[1]
			if x < np.size(im, 1) and y < np.size(im, 0):
				if cluster_im[y][x] != 255 and im[y][x] > threshold and thresholds[y][x]:
					clustertotal += im[y][x]
					cluster_im[y][x] = 255
					stack.append((x,y))
					numpixels+=1
	return float(clustertotal)/numpixels
clusters = []
for x in range(np.size(im, 1)):
	for y in range(np.size(im, 0)):
		if cluster_im[y][x]!=255 and im[y][x] > threshold and thresholds[y][x]:
			clusteravg = dfs(im, x,y)
			clusters.append(clusteravg)
		#print(clusters)
print(clusters)
plt.imshow(cluster_im, "Greys_r")
plt.show()