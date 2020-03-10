def func():
	try:
		print(5/0)
	except ZeroDivisionError:
		print("Cannot perform division, because entered expression is of the undeterminate form.")

func()
