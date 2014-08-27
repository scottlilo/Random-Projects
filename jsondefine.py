import urbandict
import json
import pprint

word = '  '
LoopEnd = False

def urbandefine(word):
	raw_data = urbandict.define(word)
	json_data = open(raw_data)
	data = json.load(raw_data)
	pprint(data)



while LoopEnd == False:
	print "-"*50
	print ("What word would you like the definition of?")
	print ("Press enter to quit.")
	print "-"*50

	if word == "":
		LoopEnd = True
		print "-"*50
		print "Program has been terminated"
		print "-"*50
	else:
		word = raw_input()
		urbandefine(word)

