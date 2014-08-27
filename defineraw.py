import urbandict

word = '  '
LoopEnd = False

def urbandefine(word):
	data = urbandict.define(word)
	
	return data

while LoopEnd == False:
	print ""
	print "-"*50
	print ("What word would you like the definition of?")
	print " "
	print ("Press enter to quit.")
	print "-"*50
	print ""
	
	if word == "":
		LoopEnd = True
		print "-"*50 
		print "Program has been terminated"
		print "-"*5
	else:
		word = raw_input()
		print urbandefine(word)

