'''c=open("demo3.txt",'a')
b="shivam"
c.write(b)
c.close()'''
def getdate():
	import datetime
	return datetime.datetime.now()

b=input("What did you ate:- ")
c=open("database.txt",'a')
d=str(getdate())
f=d + b
c.write(f)
c.close()
