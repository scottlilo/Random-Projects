file = 'file.txt'

rawfile = open(file,"a")

for x in range(1000):
	rawfile.write("I hope this fucking worked. " + str(x) + '\n')



rawfile.close()