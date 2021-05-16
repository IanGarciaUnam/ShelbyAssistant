class Neurona:
	"""
	This class will define a simple neuron 
	"""
	def __init__(self, value:int, weight:float):
		"""
		Neuron builder, i hope
		Param:
			value : value ingressed
			weight: weight assigned for each neuron 
		"""
		self.value=value
		self.weight=weight
		self.result=self.linear_fact

	def linear_fact(self):
		"""
		Returns the product of value and weight
		"""
		return self.value*weight

class Red:
	"""
	A simple neuronal network
	"""

	def __init__(self, phrase:str, layers=5, n_layers=3):
		self.phrase_value=self.convert_to_int(phrase)
		self.max_lon=len(phrase.split(" "))
		self.layers=layers
		self.n_layers=n_layers

	def convert_to_int(self, phrase):
		"""
		Convert each ASCII item to his int value, 
		then sum it with each other
			Param:
			phrase : str
			Returns:
			int value
		"""
		bonus:int=0

		items_list=list(phrase)
		for word in items_list:
			bonus+=ord(word)
		return bonus

	def think(self):
		n_longitud=Neurona(self.max_lon,0.7)
		n_ascii=Neurona(self.phrase_value, 0.3)
		




