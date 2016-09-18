import imageprocessing
import floodfill
import shapecatcherrequest
import boundingboxabs
import latex_conversion

import sys
import os

def main(image_filename):
	open('output.tex', 'w').close()
	pixel_array = imageprocessing.image_to_pixel_array (image_filename)
	line_blocks = imageprocessing.divide_lines (pixel_array)
	
	for line in range(len(line_blocks)):
		#line = line.astype(int)
		bounding_boxes = floodfill.floodfill(line_blocks[line], str(line))
		n = len(bounding_boxes)
		codes = shapecatcherrequest.unicode_list(n, str(line)) # make a dict

		print len(codes)
		print codes
		print n


		box_info, spatial_list, codes = boundingboxabs.interpret_boxes(bounding_boxes, codes) # need to debug

		latex_conversion.convert(box_info, spatial_list, codes)
	
	os.system("notepad.exe output.tex")




main(sys.argv[1])



