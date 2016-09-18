import requests  
import re


def unicode_list(n, line):

	possibilities = []
	codes = []

	for i in range(1,n+1):
		files = {'file': (open('outputimages'+line+'/outfile'+str(i)+'.png', 'rb'))}
		r = requests.post('http://shapecatcher.com/engine/engine/filepost', files = files)
		
                matches = re.findall(r'Unicode hexadecimal: 0x([0-9a-f]{4})', r.text)
                
                matches = [int(x, base=16) for x in matches]

		possibilities.append(matches)


	for i in possibilities:
		codes.append(unicodefinder(i))
		
	return codes


def unicodefinder(poss):
	forbidden = [42, 44, 46, 48, 61, 63, 75, 96, 123]
	for i in range(len(poss)):
		if ((poss[i] >= 40) and (poss[i] <= 124)):
			if poss[i] not in forbidden:
				return poss[i]



