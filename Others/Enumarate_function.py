#Enumarate function returns both index and value form a list.

l=["Shivam","Kishan","Raj"]
for index , item in enumerate(l):
	print(index)
	if index%2==0:
		print(item)
