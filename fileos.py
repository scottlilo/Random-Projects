import os

def retrieveFile():
	try:
		bestStudent ={}
		bestStudentstr = "The Best Students Ranked \n\n"

		f = open('./studentgrades.txt')

	except(IOError), e:
		print "File not found", e

	else: 
		for line in f:
			name, grade = line.split()
			bestStudent[grade] = name
		f.close()

		for i in sorted(bestStudent.keys(), reverse=True):
			print (bestStudent[i] + ' scored a ' + i)
			bestStudentstr += bestStudent[i] + ' scored a ' + i + '\n'
			print '\n'

			print bestStudentstr

			outToFile = open("studentrank.txt", "w")
			outToFile.write(bestStudentstr)
			outToFile.close()

			print "Finished Output"
		print

def main():
	retrieveFile()

if __name__ == '__main__': main()