
#赶不及了，以后有机会得重新写一遍，这个太难搞了，iterator这个概念到现在还是糊里糊涂的
class Pair:
	first = []
	second = []
	
	
	def __init__(self, first, second):
		self.first = first
		self.second = second
		self.firsts = iter(first)
		self.seconds = iter(second)
		"""
		初始化
		"""
	def __iter__(self):
		return self
	
	def __next__(self):
		if len(self.first)==0 and len(self.second)==0:
			raise StopIteration
		elif len(self.first)>0 and len(self.second)==0:
			return (next(self.firsts), None)
		elif len(self.first)==0 and len(self.second)<0:
			return (None, next(self.seconds))
		elif len(self.first)>0 and len(self.second)>0:
			return (next(self.firsts), next(self.seconds))
		

def quick_test():
	"""
	这是个小小的检测
	"""
	l = [1, 2, 3, 4, 5]
	k = [0, 9, 8, 7, 6]
	pair = iter(Pair(l, k))
	print(next(pair) == (1, 0))
	print(next(pair) == (2, 9))
	print(next(pair) == (3, 8))

