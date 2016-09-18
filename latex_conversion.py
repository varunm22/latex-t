# need to keep adding to same file, clear file at beginning of whole file

def convert(box_info, spatial_list, codes):
	latex_string = '$'
	i = 0
	while i < len(spatial_list):
		if box_info[spatial_list[i]]['frac'] != None:
			latex_string+="\\frac{"+ codes[spatial_list[i]] + '}{'
			i += 2
			latex_string+=codes[spatial_list[i]] + '}'

		elif box_info[spatial_list[i]]['equal'] != None:
			latex_string+="="
			i+=1

		elif box_info[spatial_list[i]]['super']:
			latex_string+='^'
		latex_string+= codes[spatial_list[i]]
		i += 1

	latex_string+='$ \n \n'

	text_file = open("output.tex", "a")
	text_file.write(latex_string)
	text_file.close()
	
			

