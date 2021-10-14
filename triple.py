def tripler(func):
	def wrapper():
		func()
		func()
		func()
	return wrapper

@tripler
def tripled():
	print('triple')

tripled()
