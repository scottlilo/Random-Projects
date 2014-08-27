import urbandict
index = 0
word = '  '
LoopEnd = False

def urbandefine(word):
	data = urbandict.define(word)
	word = data[index]['word']
	definition =  data[index]['def']
	example = data[index]['example']	
	print '\n' + definition
	print example + '\n'

while LoopEnd == False:
	print '\n' + '-'*50
	print ("What word would you like the definition of? \n")
	print ("Type another for a second definition of your previous entry.")
	print '\n' + ("Press enter to quit. \n") + "-"*50+'\n'
	userinput = raw_input()

	if userinput == "":
		LoopEnd = True
		print "-"*50+'\n'+"Program has been terminated. \n" + '-'*50 + '\n'
	else:
		if userinput == "another":
			index = index + 1
			urbandefine(word)
			
		else:	
			word = userinput
			urbandefine(word)

