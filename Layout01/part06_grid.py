from tkinter import *
root = Tk()
root.geometry("420x220")

def GetData():
    print(f"User Name : {user_value.get()}")
    print(f"User Pass : {pass_value.get()}")
    f = open("user_dtls","a")
    f.write(f"User Name : {user_value.get()}  User Pass : {pass_value.get()}")
    f.close()

userName = Label(root,text="Username")
userPass = Label(root,text="Password")
userName.grid(row=1)
userPass.grid(row=2)

user_value = StringVar()
pass_value = StringVar()

user = Entry(root,textvariable=user_value)
passW = Entry(root, textvariable=pass_value)

user.grid(row=1,column=2)
passW.grid(row=2,column=2)

btn = Button(text="Submit",command=GetData).grid(row=3)

root.mainloop()