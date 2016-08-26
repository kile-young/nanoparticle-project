# ThresholdDetection.py

import numpy as np
from PIL import Image
from random import randint
import matplotlib.pyplot as plt

def findThreshold(image):
	
	im = Image.open(image)
	width, height = im.size
	arr = np.array(im)

	# print 'width ', width, ' height ', height

	num_samps = width*height/1000

	rand_samps = []

	x = 0
	while x < num_samps:
		rand_pix = [randint(0,width-1), randint(0,height-1)]
		
		if rand_pix not in rand_samps:
			rand_samps.append(rand_pix)
			x += 1

	total_pix = 0.0
	rand_samps_nums = []
	
	for pix in rand_samps:
		# print pix
		total_pix += arr[pix[1]][pix[0]][0]
		rand_samps_nums.append(arr[pix[1]][pix[0]][0])

	avg_pix = total_pix/num_samps
	# print 'mean', np.mean(rand_samps_nums)
	# print 'std', np.std(rand_samps_nums)
	# print 'before', len(rand_samps_nums)
	# print 'after', len(filter(rand_samps_nums))

	while np.std(rand_samps_nums) > 10:
		rand_samps_nums = filter(rand_samps_nums)

	# print 'fin', rand_samps_nums
	changeColor(image, np.max(rand_samps_nums))
	# print rand_samps_nums
	return avg_pix

def dispColors(image):
	im = Image.open(image)
	width, height = im.size
	arr = np.array(im)

	num_samps = width*height/1000

	rand_samps = []

	x = 0
	while x < num_samps:
		rand_pix = [randint(0,width-1), randint(0,height-1)]
		
		if rand_pix not in rand_samps:
			rand_samps.append(rand_pix)
			x += 1

	total_pix = 0.0
	rand_samps_nums = []
	
	for pix in rand_samps:
		total_pix += arr[pix[1]][pix[0]][0]
		rand_samps_nums.append(arr[pix[1]][pix[0]][0])

	avg_pix = total_pix/num_samps

	colorGradient(image, rand_samps_nums)

def filter(lst):
	std = np.std(lst)
	mean = np.mean(lst)

	one_std = mean + std

	return [x for x in lst if x < one_std]


def changeColor(image, threshold):
	im = Image.open(image)
	im.load()
	im.show()
	arr = np.array(im)
	width, height = im.size
	for i in range(0, height-1):
		for j in range(0, width-1):
			if arr[i][j][0] < threshold:
				arr[i][j] = [255, 255, 0]
			else:
				arr[i][j] = [0, 0, 255]

	new_image = Image.fromarray(arr, 'RGB')
	new_image.show()


def colorGradient(image, random_lst):
	im = Image.open(image)
	im.load()
	im.show()
	arr = np.array(im)
	width, height = im.size
	std = np.std(random_lst)
	# mean = np.median(random_lst)
	# mean = np.ptp(random_lst) + np.min(random_lst)
	mean = np.mean(random_lst)

	for i in range(0, height-1):
		for j in range(0, width-1):
			pixel_value = arr[i][j][0]
			if pixel_value < mean:
				if pixel_value < mean-3*std:
					arr[i][j] = [0, 0, 255]
				elif pixel_value < mean - 2*std:
					arr[i][j] = [51, 51, 255]
				elif pixel_value < mean - std:
					arr[i][j] = [102, 102, 255]
				elif pixel_value < mean:
					arr[i][j] = [153, 153, 255]
				
			else:
				if pixel_value > mean + 3*std:
					arr[i][j] = [255, 255, 0]
				elif pixel_value > mean + 2*std:
					arr[i][j] = [255, 255, 51]
				elif pixel_value > mean + std:
					arr[i][j] = [255, 255, 102]
				elif pixel_value > mean:
					arr[i][j] = [255, 255, 153]

	new_image = Image.fromarray(arr, 'RGB')
	new_image.show()


if __name__ == '__main__':
	pic = "sample1.jpg"
	# print 'threshold: ', findThreshold(pic)
	pic2 = 'sample2.jpg'
	# print 'threshold2: ', findThreshold(pic2)
	dispColors(pic)
	dispColors(pic2)



