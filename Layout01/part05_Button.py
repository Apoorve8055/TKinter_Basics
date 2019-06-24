from tkinter import *
def BtnFun():
    exit(0)
def Hellow():
    print("Hellow Apoorv")
root = Tk()
root.geometry("420x220")
root.title("Button Functioning")
F1 = Frame(root,bg="yellow",borderwidth=3)
F1.pack(fill=X)
Hellow_btn = Button(F1,text="Hellow",command=Hellow)
Hellow_btn.pack(side=LEFT,anchor="sw")
Exit_btn = Button(F1,text="Exit",command=BtnFun)
Exit_btn.pack(side=LEFT,anchor="sw")
root.mainloop()
