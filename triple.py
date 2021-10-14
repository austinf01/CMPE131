def tripler(func):
	func()
	func()
	func()

@tripler
def tripled():
	print("triple")

