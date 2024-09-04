import inspect
from math import sqrt

class Person(object):
	"""docstring for Person"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def __str__(self):
		return f"{self.name} {self.age}"


person = Person('Jeffrey', 34)
all_func = inspect.getmembers(Person, inspect.isfunction)

# for func in all_func:
# 	print(func[1])

def example_function(a, b=2, *args, **kwargs):
	"""This is an example function."""
	print (a, b)
sig = inspect.signature(example_function)
# print(sig)

argspec = inspect.getfullargspec(example_function)
# print(argspec)
# print(type(sig), type(argspec), argspec)

doc = inspect.getdoc(example_function)
# print(doc)
source = inspect.getsource(example_function)
# print(source)


module = inspect.getmodule(sqrt)
# print(module)

members = inspect.getmembers(Person)
# print(members)

# print(inspect.ismethod(example_function))
# print(inspect.isfunction(example_function))

frame = inspect.currentframe()
# print(frame)

# def first():
# 	second()

# def second():
# 	print(inspect.stack())

# first()

print(inspect.isclass(Person))
import math
print(inspect.ismodule(math))
line_no, source_lines = inspect.findsource(Person)
print(f'starts at line: {line_no}')
