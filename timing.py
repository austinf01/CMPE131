import time

def timer(func):
	startTime = time.time()							#retrieves time before function run
	func()									#runs start() function
	print("Total time:", "%.2f" % round(time.time() - startTime, 2), "seconds")	#prints time after function run - time before function run
	
@timer
def start():
	time.sleep(2)


