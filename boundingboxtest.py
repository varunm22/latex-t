def interpret_boxes(boxes, codes):

	spatial = {}

	box_dict = {}

	max_x = 0
	max_y = 0


	for box in boxes:
		tl, br = box
		ty, tx = tl
		by, bx = br


		if bx > max_x:
			max_x = bx
		if by > max_y:
			max_y = by


		spatial[float(tx+bx)/2] = box

		print box, max_x
	
	print max_x

	interval_left = [None]*(max_x+1)
	interval_right = [None]*(max_x+1)
	interval_level = [None]*(max_x+1)

	for box in boxes:
		tl, br = box
		ty, tx = tl
		by, bx = br

		interval_left[tx] = box
		interval_right[bx] = box




	layers = []
	fractions = set()

	for i in range(max_x+1):
		if interval_left[i] != None:
			layers.append(interval_left[i])
		if interval_right[i] != None:
			print layers, i
			del layers[layers.index(interval_right[i])]

		interval_level[i] = layers
		if len(layers) == 3:
			fractions.add((layers[0], layers[1], layers[2]))

	spatial_list = sorted(spatial.keys())
	spatial_boxes = []

	for i in range(len(spatial_list)):
		box_dict[spatial[spatial_list[i]]] = {'pos': i, 'super':  False, 'sub' : False, 'frac': None, 'equal' : None}
		spatial_boxes.append(spatial[spatial_list[i]])


	for box in boxes: 
		tl, br = box
		ty, tx = tl
		by, bx = br
		pos = box_dict[box]['pos']

		if by < max_y/2 and pos >= 1:
			box_dict[box]['super'] = True

		if ty > max_y/2 and pos >= 1:
			box_dict[box]['sub'] = True

	for frac in fraction:
		a, b, c = frac
		frac_list = [a,b,c]
		frac_list.sort(key=lambda x: x[0][1], reverse=True)
		
		for i in frac_list:
			box_dict[i]['frac'] = frac_list

	
	return box_dict, spatial_boxes, codes





	




