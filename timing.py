import time

def calculate_time(func):
	startTime = time.time()							#retrieves time before function run
	func()									#runs start() function
	return ("Total time:", "%.2f" % round(time.time() - startTime, 2), "seconds")	#returns time after function run - time before function run

@calculate_time
def start():
	time.sleep(2)


