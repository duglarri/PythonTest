def saydate():
	x = "test"
	y = 2

	import datetime

	x = datetime.datetime.now()
	print(x)

	print(x.year) 
	print(x.strftime("%A"))
	return "this is my return value"
