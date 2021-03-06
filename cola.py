import Queue

class Cola(object):
	"""
	Implementacion de cola con los metodos necesarios para utilizar el iterador del grafo
	"""

	def __init__(self):
		self.elementos = Queue.Queue()
		self.tam = 0

	def encolar(self,elemento):
		self.elementos.put(elemento)
		self.tam += 1
		return True

	def desencolar(self):
		"""
		desencolar devuelve nulo si la cola esta vacia y
		el elemento si esta no lo esta
		"""
		if self.esta_vacia():
			return None
		elem = self.elementos.get()
		self.tam -= 1
		return elem

	def esta_vacia(self):
		return self.tam == 0
