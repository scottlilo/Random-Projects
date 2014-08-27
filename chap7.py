globalTen = 10
def factorial(num):
	if num == 1:
		return 1
	else: 
		return num * factorial(num-1)

def main():
	print factorial(10)


if __name__ == '__main__': main()