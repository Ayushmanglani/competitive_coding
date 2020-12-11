'''
Iterators allow us to create and work with lazy iterable which means you can use an iterator for the lazy evaluation. This allows you to get the next element in the list without re-calculating all of the previous elements. Iterators can save us a lot of memory and CPU time.

Python has many built-in classes that are iterators, e.g — enumerate, map ,filer , zip and reversed etc. objects are iterators.

Python iterator objects are required to support two methods while following the iterator protocol.
__iter__ returns the iterator object itself. This is used in for and in statements.
__next__ method returns the next value from the iterator. If there is no more items to return then it should raise StopIteration exception.
'''
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