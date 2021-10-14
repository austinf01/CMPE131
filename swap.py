def swap_last_item(arg):
	temp = arg[0]			#stores first element of list 
	maxIndex = len(arg) - 1		#stores last index of list
	arg[0] = arg[maxIndex]		#sets first element to last element
	arg[maxIndex] = temp		#sets last element to first element
	return arg			#returns new list

