from tkinter import *

def submit():
    msg = "Hello " + textname.get()
    lbmsg.config(text=msg) 

def showForm():
    global root, textname, subbtn, lbmsg
    root = Tk()
    root.geometry("1000x600")
    root.option_add("*Font", "Arial 14 bold")
    lbname = Label(root, text="Enter Name:")
    lbname.place(relx=0.05, rely=0.05)
    textname = Entry(root)
    textname.place(relx=0.2, rely=0.05)
    subbtn = Button(root, text="Submit", command=submit)
    subbtn.place(relx=0.1, rely=0.1)
    lbmsg = Label(root, text="") 
    lbmsg.place(relx=0.05, rely=0.2)
    root.mainloop()
showForm()
