'''
A decorator in Python is any callable Python object that is used to modify a function or a class. It takes in a function, adds some functionality, and returns it. Decorators are a very powerful and useful tool in Python since it allows programmers to modify/control the behavior of function or class. Decorators are usually called before the definition of a function you want to decorate. There are two different kinds of decorators in Python:

Decorator is way to dynamically add some new behavior to some objects.
'''

def div(a,b):
	return a/b

def smart_div(func):

	def inner(a,b):
		if a<b:
			a,b = b,a
		return func(a,b)
	return inner

div = smart_div(div)

print(div(5,10))

'''
def test_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper
@test_decorator
def sqr(n):
    return n ** 2
sqr(54)
'''