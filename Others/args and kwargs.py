def myfunction(normal,*list2,**disc):    #Normal , args then kwargs
	print(normal)
	

	for i in list2: #Using **kwargs
		print(i)
	

	for key,value in disc.items():   #Using **kwargs
		print(f"{ key } is {value}")

l=["Shivam","Kishan","Ganesh"]
d={"Shivam":"Head","Kishan":"Subhead"}
n="This is an example of *args and **kwara."
myfunction(n,*l,**d)