class Animal:

	animal_count=0

	@classmethod
	def display_animal_count(cls):
		return f'There are a total of {cls.animal_count} animals'

	def __init__(self, name, color, species):
		self.name = name
		self.species = species
		Animal.animal_count+=1
	
	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def get_color(self):
		return f'{self.name} is of color {self.color}'


class Cat(Animal): #inherits Animal class

	cat_count=0

	@classmethod
	def display_cat_counts(cls):
		return f'There are a total of {cls.cat_count} animals'


	def __init__(self, name, color, toy):
		super().__init__(name, color, species='Cat')  #since Cat inherits Anaimal class, no need to specify Species to Cat __init__ mehod, super() will cal Animal init method 
		#Animal.__init__(name,species='Cat')
		self.toy = toy
		Cat.cat_count+=1
		
	def play(self):
		return f"{self.name} plays with {self.toy}"

	def __repr__(self):
		return f'{self.name} is {self.species} {self.color} in color'



class Dog(Animal): #inherits Animal class
	def __init__(self, name, color, food): #just add extra food attribute , rest of the common stuff is done by super by calling the parent class
		super().__init__(name, color, species='Dog') 
		self.food=food

	def meal(self):
		return f"{self.name} likes to eat {self.food}"


print(Animal.display_animal_count())
blue = Cat('Blue', 'black','string')
print(blue.play())
print(Cat.display_cat_counts())


big = Dog('Big', 'brown','munchies')
print(big.meal())

#Both Cat and Dog are instances of Animal. To prove print below
print(isinstance(blue, Cat)) 
print(isinstance(big, Dog))
