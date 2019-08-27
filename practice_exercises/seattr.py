class Animal:
	descriptions = {}

	
	def __init__(self, name, colors, sounds):
		self.name = name
		self.descriptions['color']=colors
		self.descriptions['sound']=sounds

	#def color_values(self):
		#print(f"{self.name}:{self.descriptions['color']}")
	


	def add_description_fn(self,description):

		fn_name = description + '_values'
		print(f"function name : {fn_name}")
		def fn(self):
			print(f"{self.name}:{self.descriptions[description]}")
		setattr(Animal, fn_name, fn)

		


description_names = {'color', 'sound'}

cat = Animal('cat1', colors=['red','orange'], sounds=['purr','meow'])
print(cat.descriptions)

for description in description_names:
	cat.add_description_fn(description)

print(cat.color_values())
print(cat.sound_values())