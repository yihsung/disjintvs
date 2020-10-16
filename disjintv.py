class DisjIntvs():
	def __init__(self, intvs=[]):
		if not intvs:
			self.intvs = []
		else:
			for a, b in intvs:
				self.add(a, b)

	
	def __str__(self):
		return str(self.intv)

	def add(a, b):
		return

	def remove(a, b):
		return


class Operator():
	def __init__(self, intvs=[], acts=[])
		self.intvs = DisjIntvs(intvs) # maintian a set of intervals

		self.acts = acts # maintian a set of actions

	
	def load(): # load commands from a file
		return


	def run():
		for com, a, b in self.acts:
			



A = DisjIntvs()
A.intvs = [[1, 2], [3, 4]]
print(A.intvs)
