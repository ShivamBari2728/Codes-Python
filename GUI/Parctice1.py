from tkinter import *
from PIL import Image , ImageTk

shivam_root = Tk()              #Making object

shivam_root.geometry("400x400") #window size

shivam_root.minsize(200,200)    #Minimum Size

shivam_root.maxsize(600,600)    #Maximum Size

sky = Label(text="This is GUI")
sky.pack()                      #pack to view
phot = Image.open("pho.jpg")
pic = ImageTk.PhotoImage(phot)
sky2 = Label(image=pic)
sky2.pack()

shivam_root.mainloop()          #Last line