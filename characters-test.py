import sys
import floodfill
import imageprocessing
import numpy as np

def main():
	init_array = imageprocessing.image_to_pixel_array('examples/eq3.jpg')
	array = init_array.astype(int)
	#np.savetxt('test.out',array,fmt='%d',delimiter='')
	characters = floodfill.floodfill(array)
	print characters


main()
