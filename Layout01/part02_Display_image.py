from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.geometry("520x420")
root.maxsize(720,480)
root.minsize(420,220)

#img = PhotoImage(file="avatar.png")

img = Image.open("img1.jpg")
photo = ImageTk.PhotoImage(image=img)

label2 = Label(image=photo)
label2.pack()

root.mainloop()