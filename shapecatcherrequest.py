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

	for i in range(len(possibilities)):  
		if len(possibilities[i]) == 0:
			possibilities[i] = [45]


	for i in possibilities:
		print i
		codes.append(unicodefinder(i))
		
	return codes


def unicodefinder(poss):
	#The characters we really care about are like normal letters  and digits
	symboldict = {79:'a',586:'a',587:'a',593:'a',945:'a',6514:'a',9082:'a',11373:'a',2005:'b',4334:'b',98:'b',1068:'b',
               5234:'b',7509:'b', 7529:'b',1010:'c',99:'c',5222:'c',8573:'c',67:'c',7428:'c',5776:'c',5231:'d',100:'d',1280:'d',
               120253:'d',9474:'1',124:'1',9145:'1',9144:'1', 8739:'1',12518:'2',1334:'2',120824:'2',50:'2',7550:'2',1353:'2',
               12777:'2',42843:'2',51:'3',12825:'3',120825:'3',120805:'3',1047:'3',179:'3', 604:'3', 1079:'3', 1069:'3', 43:'+',
               11612:'+',9532:'+',5776:'+',120827:'5', 8488:'3', 52:'4', 5070:'4', 9029:'4', 120826:'4', 120806:'4', 120796:'4',
               8308:'4', 120827:'5', 53:'5', 120807: '5', 1172:'5', 8513:'5',11791:'-',8213:'-',9149:'-'}
	#forbidden = [42, 44, 46, 48, 61, 63, 75, 96, 123]
	for i in range(len(poss)):
		#if ((poss[i] >= 40) and (poss[i] <= 124)):
		#	if poss[i] not in forbidden:
		#		return poss[i]
		if poss[i] in symboldict:
			return symboldict[poss[i]]
	return '-'

