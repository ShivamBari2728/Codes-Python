numi=input("Enter value of num1: ")
num2=input("Enter value of num2: ")
try:
	print("Addition of values is : ", int(num1)+int(num2))
except Exception as a:
	print(a)

print("The error is passed.")
	