
__metaclass__ = type

class Animal:

	__name = "No Name"
	__owner = "No Owner"

	def __init__(self, **kvargs):
		self.attributes = kvargs

	def set_attributes(self, key, value):
		self.attributes[key] = value	
		return	

	def get_attributes(self,key):
		return self.attributes.get(key,none)

	def noise(self):
		print('errr')
		return

	def move(self):
		print('The animal moves forward')
		return

	def eat(self):
		print('Crunch, Crunch')
		return


class Dog(Animal):
	def __init__(self, **kvargs):
		super(Dog, self).__init__()
		self._attributes = kvargs
	def noise(self):
		print ('Woof, Woof')
		Animal.noise(self)

class Cat(Animal):
	def __init__(self, **kvargs):
		super(Cat,self).__init__()
		self.attributes = kvargs	
	def noise(self):
		print("Meow")
		return
	def noise2(self):
		print ('Purrrr')
		return

def playwithanimal(animal):	
	animal.eat()
	animal.noise()
	animal.move()
	print(animal.get_attributes('__name'))
	print(animal.get_attributes('__owner'))

def main():
	jake = Dog(__name='Jake', __owner='Paul')
	sophire = Cat(__name='Sophie', __owner='Sue')
	playwithanimal(sophie)
	playwithanimal(jake)
	
if __name__ == '__main__': main()
