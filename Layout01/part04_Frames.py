from tkinter import *
root = Tk()
root.geometry("720x620")
root.title("Layout of Pycharm")
Menu_Frame = Frame(root , bg="grey" , borderwidth=3)
Menu_Frame.pack(side=TOP , fill=X)
Sidebar_Frame = Frame(root , bg="grey" , borderwidth=3)
Sidebar_Frame.pack(side=LEFT,fill=Y)
File_button = Button(Menu_Frame,text="File").pack(fill=Y,side=LEFT)
Edit_button = Button(Menu_Frame,text="Edit").pack(fill=Y,side=LEFT)
About_button = Button(Menu_Frame,text="About").pack(fill=Y,side=LEFT)

root.mainloop()