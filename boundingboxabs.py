def interpret_boxes(boxes, codes):
	#boxes is a list of twouples of twoples that tells you size and position of boxes
	#codes is a list of strings corresponding to each box. The order is the SAME

	#First get max x and min x. Then, for each endpoint, check to see which elements are currently 
	#in the list. If there are multiple minuses, then do things. If there's one minus and over 3 things, 
	# do different things. 

	#Basically, you just want to output a horizontally sorted sequence unicode things, with the 
	#additional information of whether or not a particular block is in a fraction, sup/subscript
	#or is an equals.  
	unicodedict = {}
	for i in range(len(boxes)):
		unicodedict[boxes[i]] = codes[i]
	
	
	max_y = 0
	min_y = 4000

	endpoints = []
	for box in boxes:
		tl, br = box
                ty, tx = tl
                by, bx = br
		
		min_y = min(min_y,by)
		max_y = max(max_y,ty)
		
		endpoints.append((tx,0,box))
		endpoints.append((bx,1,box))

	threshold = (float(max_y)/2)
	
	boxes = sorted(boxes,key=lambda x: x[0][1])
	endpoints = sorted(endpoints,key=lambda x: x[0])
	print "Endpoints are"
	print endpoints	
	#Now we should have a list of boxes sorted by left edge x
	#As well as a list of endpoints sorted by x position
	#We should run through the list, checking to see if things are superscript/subscript
	#We should keep track of what things are actually in the list of symbols present rn
	
	#superscripts = []
	for box in boxes:
                tl, br = box
                ty, tx = tl
                by, bx = br
                
		#if by>threshold:
		#	superscripts.append(1)
		#else:
		#	superscripts.append(0)
	
	
	layer_count = 0
	minus_count = 0
	#layers = []
	#minus = []

	box_dict = {}
	j=0

	#keyed by two(twople)ple
	#position, superscript, subscript, [top equal, bottom equal], [top frac, bar frac, bot frac]
	print "Start parsing!"
	for i in range(len(endpoints)):
		#Basically, hash the endpoints by the box that they contain and maintain a "minus counter",
		#a "layer counter", and basically your output should be a series of unique "items"
		# that the latex can print
		if endpoints[i][1] == 0:
			#Start endpoint
			superscript = False
			subscript = False
			if unicodedict[endpoints[i][2]] == '-':
				minus_count += 1
			layer_count += 1
			if endpoints[i][2][1][0] < threshold:
				superscript = True

			box_dict[endpoints[i][2]] = {'pos': j, 'super': superscript, 'equal': None, 'frac': None, 'text': unicodedict[endpoints[i][2]]}
			j += 1
			print unicodedict[endpoints[i][2]]

		if layer_count == 3:
			box_dict[endpoints[i][2]][frac] = [endpoints[i-2][2],endpoints[i-1][2],endpoints[i][2]]
			box_dict[endpoints[i-1][2]][frac] = [endpoints[i-2][2],endpoints[i-1][2],endpoints[i][2]]
			box_dict[endpoints[i-2][2]][frac] = [endpoints[i-2][2],endpoints[i-1][2],endpoints[i][2]]
 
		if minus_count == 2:
			box_dict[endpoints[i][2]][equal] = [endpoints[i][2],endpoints[i-1][2]]
			box_dict[endpoints[i-1][2]][equal] = [endpoints[i][2],endpoints[i-1][2]]			
		
		
		else:
			if unicodedict[endpoints[i][2]] == '-':
				minus_count -= 1
			layer_count -= 1
	
	print "Box dict is: "
	print box_dict
	print "Boxes in horizonatlly sorted order are: "
	print boxes
	print "Unicode dictionary is: "
	print unicodedict
	return box_dict, boxes, unicodedict
			
			
		 
		
