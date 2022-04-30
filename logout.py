from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("550x500")

def logout():
    r=messagebox.askyesnocancel(title="Exit",message="Are you sure?")
    if(r==1):root.logout
btn1=Button(text="Log out",command=logout)
btn1.pack()
root.mainloop()