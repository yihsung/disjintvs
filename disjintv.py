class DisjIntvs():
	def __init__(self, intvs=[]):
		# the intervals are kept in the format of [a, b]
		# add artificial negative infinity and positive infinity to simplify the code
		self.intvs = [[-float("inf"), -float("inf")], [float("inf"), float("inf")]]

		if intvs:
			for a, b in intvs:
				self.add(a, b)

	
	def __str__(self):
		n = len(self.intvs)
		return str(self.intvs[1:n-1])
	

	def _find(self, i, t): # i=0:left end, i=1:right end; t: traget val
		# binary search
		lo, hi = 0, len(self.intvs)-1 
		
		while lo <= hi:
			mid = (lo+hi) // 2

			if self.intvs[mid][i] == t:
				return mid
			elif t < self.intvs[mid][i]:
				hi = mid - 1
			else:
				lo = mid + 1

		return lo


	def add(self, a, b):
		print("+", a, b)
		
		if len(self.intvs) == 2: # no intvs stored
			self.intvs = [self.intvs[0]] + [[a, b]] + [self.intvs[1]]
			#print(self.intvs)
			print(self.__str__())
			return

		# find the lower and upper index
		i, j, n = self._find(0, a), self._find(1, b), len(self.intvs)

		if i > 0 and a <= self.intvs[i-1][1]:
			i -= 1

		if 0 < j < n and b < self.intvs[j][0]:
			j -= 1
		
		a1, b1 = min(self.intvs[i][0], a), max(self.intvs[j][1], b)
		self.intvs = self.intvs[:i] + [[a1, b1]] + self.intvs[j+1:]
	
		#print(self.intvs)
		print(self.__str__())
		return


	def remove(self, a, b):
		print("-", a, b)
		
		if len(self.intvs) == 2: # no intv stored
			#print(self.intvs)
			print(self.__str__())
			return # do nothing

		# find the lower and upper index
		i, j, n = self._find(1, a), self._find(0, b), len(self.intvs)

		if i > 0 and a <= self.intvs[i-1][1]:
			i -= 1

		if 0 < j < n and b < self.intvs[j][0]:
			j -= 1
		
		b1, a1 = min(self.intvs[i][1], a), max(self.intvs[j][0], b)

		if a1 < self.intvs[j][1]:
			self.intvs = self.intvs[:i] + [[self.intvs[i][0], b1]] + [[a1, self.intvs[j][1]]] + self.intvs[j+1:]
		else:
			self.intvs = self.intvs[:i] + [[self.intvs[i][0], b1]] + self.intvs[j+1:]
		
		#print(self.intvs)
		print(self.__str__())
		return


class Operator():
	def __init__(self, intvs=[], acts=[]):
		self.intvs = DisjIntvs(intvs) # maintian a set of intervals

		self.acts = acts # maintian a set of actions

	
	def load(self): # load commands from a file
		return


	def run(self):
		for com, a, b in self.acts:
			if com: # com=1: add
				self.intvs.add(a, b)
			else: # com=0: remove
				self.intvs.remove(a, b)
				

	def result(self):
		print(self.intvs)


# main
A = [[1,1,5],[1,6,8],[1,3,5],[1,5,6]]
A = [[1,1,8],[0,3,9]]
A = [[1,2,5],[0,3,4]]
opt = Operator(acts=A)
opt.run()
#opt.result()
