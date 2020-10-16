import disjintv1
import random

##########################################################

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

		if a == b: # invalid interval, do nothing
			return 
		
		if len(self.intvs) == 2: # no intvs stored
			self.intvs = [self.intvs[0]] + [[a, b]] + [self.intvs[1]]
			print(self.__str__())
			return

		# find the lower and upper index
		i, j, n = self._find(0, a), self._find(1, b), len(self.intvs)

		if i > 0 and a <= self.intvs[i-1][1]:
			i -= 1

		if 0 < j < n and b < self.intvs[j][0]:
			j -= 1
		
		a1, b1 = min(self.intvs[i][0], a), max(self.intvs[j][1], b)
		self.intvs[i:j+1] = [[a1, b1]]
	
		print(self.__str__())
		return


	def remove(self, a, b):
		print("-", a, b)
		
		if a == b: # invalid interval, do nothing
			return 

		if len(self.intvs) == 2: # no intv stored
			print(self.__str__())
			return # do nothing

		# find the lower and upper index
		i, j, n = self._find(1, a), self._find(0, b), len(self.intvs)

		if i > 0 and a <= self.intvs[i-1][1]:
			i -= 1

		if 0 < j < n and b < self.intvs[j][0]:
			j -= 1
		
		b1, a1 = min(self.intvs[i][1], a), max(self.intvs[j][0], b)

		if self.intvs[i][0] < b1 and a1 < self.intvs[j][1]:
			self.intvs[i:j+1] = [[self.intvs[i][0], b1]] + [[a1, self.intvs[j][1]]]
		elif self.intvs[i][0] < b1:
			self.intvs[i:j+1] = [[self.intvs[i][0], b1]]
		elif a1 < self.intvs[j][1]:
			self.intvs[i:j+1] = [[a1, self.intvs[j][1]]]
		else:
			self.intvs[i:j+1] = [] 
		
		print(self.__str__())
		return

#----------------------------------------------------------

class Operator():
	def __init__(self, intvs=[], acts=[]):
		self.intvs = DisjIntvs(intvs) # maintian a set of intervals

		self.acts = acts # maintian a set of actions

	
	# for future expansion
	#def load(self): # load commands from a file
	#	return

	
	def gen_randtest(self):
		TESTCMDS = 5 # number of test cases
		UPPBDD = 20 # upper bound of the interval
		temp = []

		N = random.randint(1, TESTCMDS) 
		for _ in range(N):
			c = random.randint(0, 1)
			a, b = random.randint(0, UPPBDD), random.randint(0, UPPBDD)
			if a > b:
				a, b = b, a
			temp.append([c, a, b])

		self.acts = temp


	def run(self):
		for com, a, b in self.acts:
			if com: # com=1: add
				self.intvs.add(a, b)
			else: # com=0: remove
				self.intvs.remove(a, b)
				

	def result(self):
		#print(self.intvs)

		return self.intvs.__str__()


##########################################################

# main section

# random test
ROUNDS = 10 # test rounds
c = 0 # count

for _ in range(ROUNDS):
	# first operator
	opt = Operator()
	opt.gen_randtest()
	opt.run()
	#opt.result()

	print("----")
	
	# second operator
	A = opt.acts # export the commands for operator1 to test
	opt1 = disjintv1.Operator(acts=A) # second approach for justify the result
	opt1.run()

	c += opt.result()==opt1.result()

	print("-------------")

print("different cases: %d\n" % (ROUNDS-c)) # print out number of different cases

# test 1
A = [[1,1,5],[0,2,3],[1,6,8],[0,4,7],[1,2,7]]

opt = Operator(acts=A)
opt.run()

