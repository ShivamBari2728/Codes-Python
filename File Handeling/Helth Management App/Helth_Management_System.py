print("            (ᵔ◡ᵔ)🏋Habit Tracker🍲(ᵔ◡ᵔ)\n\n")
def getdate():
	import datetime
	return datetime.datetime.now()

def main_menue():
	print("             -------------Main Menue-------------")
	a=input("🔹Enter Your Choice.... \n1 - 📝To log information \n2 - 🖨️To retrive information \nPress any other key to exit :- ")
	if (a=="1"):
		log()
	elif (a=="2"):
			retrive()

	else :
			print("❌Exiting Program....")


def log():
	print("             -----------📝Log Information-----------")
	print("🔹Enter your choice...\n1- 🍲Diet Entry\n2- 🏋Exercise Entry\n")
	a=int(input("🔹Enter your choice:- "))
	if a==1:
		diet()
	elif a==2:
		exercise()

def diet():
	print("             -----------🍲Diet Menue-----------")
	b=input("What did you ate:- ")
	temp=name+".txt"
	c=open(temp,'a')
	d=str(getdate())
	f="\nDate and Time of Entry:- " + d + "(Diet)--->" + b +"\n"
	c.write(f)
	c.close()
	main_menue()


def exercise():
	print("             -----------🏋Exercise Menue-----------")
	b=input("What Exercise did you did :- ")
	temp=name+".txt"
	c=open(temp,'a')
	d=str(getdate())
	f="\nTiming and date of Entry:- "+ d + "(Exercise)--->" + b +"\n"
	c.write(f)
	c.close()
	main_menue()

def retrive():
	print("\n\n\n             -----------🖨️Here is your log information-----------")
	temp=name+".txt"
	iv= open(temp)
	c=iv.readlines()
	for i in c:
		print(i)
	main_menue()




def login():
    print("🔹Enter Name OF User.")
    global name
    name=input("Your name (First Letter Capital) :- ")
    print("Welcome "+name+" !!!")
    main_menue()
login()
