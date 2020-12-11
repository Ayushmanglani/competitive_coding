'''
Generator functions act just like regular functions with just one difference that they use the Python yield keyword instead of return . A generator function is a function that returns an iterator. A generator expression is an expression that returns an iterator. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop.
A return statement terminates a function entirely but a yield statement pauses the function saving all its states and later continues from there on successive calls.
'''

def topten():
	val = 1
	while val<=10:
		yield val
		val += 1
	yield val

values = topten()
while True:
	try:
		print(values.__next__())
	except:
		break
'''
for i in values:
	print(i)
'''