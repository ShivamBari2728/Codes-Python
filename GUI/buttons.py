from tkinter import *
root = Tk()
root.geometry("500x500")

def click():
    print("Botton clicked..")

f1=Frame(root,borderwidth=9)
f1.pack(side=TOP,anchor=NW)

b1=Button(f1,command=click,text="Click here")
b1.pack()

root.mainloop()