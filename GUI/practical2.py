from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Practicl 2")

f= Frame(root,bg="red",borderwidth=9,relief=SUNKEN,height=50)
f.pack(side=LEFT,fill=Y)

f2 = Frame(root,bg="gray",borderwidth=8)
f2.pack(side=TOP,fill=X)

l = Label(f,text="Hiii",width=15)
l.pack()

l2 = Label(f2,text="Welcome to my window.",font="Arial 16", fg="red")
l2.pack()

root.mainloop()