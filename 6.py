#Display the divide by zero error using  try and except#
try:
	num1=int(input("Enter a first val:"))
	num2=int(input("Enter a sec val:"))
	res=num1/num2
	print("result is:",res)
except ZeroDivisionError:
 	print("cant divide by zero")
except ValueError:
	print("Enter integer val")
 

