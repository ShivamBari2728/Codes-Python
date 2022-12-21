from tkinter import *
root = Tk()


def view():
    print(f"Username is :- {uservalue.get()}")
    print(f"Username is :- {passvalue.get()}")


user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

A=Entry(root,textvariable=uservalue)
B=Entry(root,textvariable=passvalue)
A.grid(row=0,column=1)
B.grid(row=1,column=1)


Butt = Button(text="Login",command=view)
Butt.grid()

root.mainloop()