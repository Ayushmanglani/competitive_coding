class TopTen:

	def __init__(self):
		self.val = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.val <= 10:
			num = self.val
			self.val += 1

			return num
		else:
			raise StopIteration

values = TopTen()

# print(next(values))

for i in values:
	print(i)

'''	

num = [10,4,5,6,1]

numIt = num.__iter__()

for n in numIt:
	print(n)

'''