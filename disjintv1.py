import bisect


class DisjIntvs():
	def __init__(self, intvs=[]):
		self.intvs = []

		if intvs:
			for a, b in intvs:
				self.add(a, b)

	
	def __str__(self):
		n = len(self.intvs)
		ret = [[self.intvs[i], self.intvs[i+1]] for i in range(0, n, 2)]
		
		return str(ret)
	

	def add(self, a, b):
		print("+", a, b)
		
		if a == b: # invalid interval, do nothing
			return 

		if not self.intvs: # no intvs stored
			self.intvs = [a, b]
			#print(self.intvs)
			print(self.__str__())
			return

		# find the lower and upper index
		i = bisect.bisect_left(self.intvs, a) 
		j = bisect.bisect_right(self.intvs, b)

		temp = []
		if i % 2 == 0:
			temp.append(a)

		if j % 2 == 0:
			temp.append(b)
		
		self.intvs[i:j] = temp 
	
		print(self.__str__())
		return


	def remove(self, a, b):
		print("-", a, b)
		
		if a == b: # invalid interval, do nothing
			return 

		if not self.intvs: # no intv stored
			#print(self.intvs)
			print(self.__str__())
			return # do nothing

		# find the lower and upper index
		i = bisect.bisect_left(self.intvs, a) 
		j = bisect.bisect_right(self.intvs, b)

		temp = []
		if i % 2 == 1:
			temp.append(a)
		
		if j % 2 == 1:
			temp.append(b)

		self.intvs[i:j] = temp

		print(self.__str__())
		return


class Operator():
	def __init__(self, intvs=[], acts=[]):
		self.intvs = DisjIntvs(intvs) # maintian a set of intervals

		self.acts = acts # maintian a set of actions

	
	def run(self):
		for com, a, b in self.acts:
			if com: # com=1: add
				self.intvs.add(a, b)
			else: # com=0: remove
				self.intvs.remove(a, b)
				

	def result(self):
		#print(self.intvs)

		return self.intvs.__str__()


# main section
if __name__ == '__main__':
	A = [[1,1,5],[1,6,8],[1,3,5],[1,5,6]]
	#A = [[1,1,8],[0,3,9]]
	#A = [[1,2,5],[0,3,4]]
	opt = Operator(acts=A)
	opt.run()
