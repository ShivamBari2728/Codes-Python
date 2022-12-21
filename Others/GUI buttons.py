import tkinter
from tkinter import *
root=Tk()
var = StringVar()
itv1=Message(root,textvariable=var,relief=RAISED)
var.set("Welcome to itvoygers.in")
itv1.pack()
def helloCallBack():
    tkinter.messagebox.showinfo("I am title","Enjoy learning with itvoyagers")
B=tkinter.Button(root,text="Click Me", command=helloCallBack)
B.pack()
