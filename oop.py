
class Animal:

	hungry = "Yes"
	name = "No Name"
	owner = "No Owner"

	def __init__(self):
		pass

	def set_owner(self, newOwner):
		self.owner = newOwner
		return

	def get_owner(self):
		return self.owner

	def set_name(self, newName):
		self.name = newName

	def get_name(self):
		return self.name

	def noise(self):
		print('errr')
		self.__hiddenmethod()
		return

	def __hiddenmethod(self):
		print ("Hard to find")

def main():
	dog = Animal()

	dog.set_owner('Sue')
	print dog.get_owner()
	dog.set_name('rex')
	dog.noise()
	print dog.get_name()
	


if __name__ == '__main__': main()