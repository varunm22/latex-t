import imageprocessing
import floodfill
import shapecatcherrequest
import boundingboxtest

def main(image_filename):
	pixel_array = imageprocessing.image_to_pixel_array (image_filename)
	line_blocks = imageprocessing.divide_lines (pixel_array)
	
	for line in range(1): #range(len(line_blocks)):
		#line = line.astype(int)
		bounding_boxes = floodfill.floodfill(line_blocks[line], str(line)) 
		n = len(bounding_boxes)
		codes = shapecatcherrequest.unicode_list(n, str(line))

		print len(codes)
		print codes
		print n


		box_info = boundingboxtest.interpret_boxes(bounding_boxes, codes) # need to add equals and debug


main('examples/eq4.jpg')



