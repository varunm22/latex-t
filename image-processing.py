from PIL import Image
from PIL import ImageEnhance
import numpy as np


def image_to_pixel_array (image_filename):
	im = Image.open(image_filename)

	enhancer = ImageEnhance.Contrast(im)

	im = enhancer.enhance(2.0)

	ix = im.load()


	for i in range(im.size[0]):
		for j in range(im.size[1]):
			if sum(ix[i,j])/3.0 > 60: 
				ix[i,j] = (256, 256, 256)
			else:
				ix[i, j] = (0,0,0)

	l = []

	for i in range(1,im.size[0]-1):
		for j in range(1,im.size[1]-1):
			if sum ([ix[i+1, j+1] == (0,0,0), ix[i-1, j+1] == (0,0,0), ix[i+1, j-1] == (0,0,0), ix[i-1, j-1] == (0,0,0)]) > 1:
				l.append((i, j))

	for i in l:
		ix[i[0], i[1]] = (0,0,0)
	
	final_array = np.zeroes([im.size[1], im.size[0]], int)

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			final_array[j, i] = ix[i, j]

	return final_array

def divide_lines(full_array):

	line_blocks = []

#	sums = 

	return line_blocks


def main (image_filename):
	image_to_pixel_array(image_filename)


main('examples/eq3.jpg')





