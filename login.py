from cProfile import label
from tkinter import*
from turtle import title
from PIL import ImageTk
from tkinter import messagebox
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        #===images================
        self.phone_image=ImageTk.PhotoImage(file="images/internet.jpg")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=0,y=0)

        #===========login_frame==========
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold")).place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        btn_forget=Button(login_frame,text="Forgot Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)
        
        
    def login(self):    
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.username.get()!="ICT" or self.password.get()!="15":
            messagebox.showerror("Error","Invalid Usernam or Password\n Try again with correct credentials")
        else:
            messagebox.showinfo("information",f"Welcome : {self.username.get()}")
            self.root.destroy()
            os.system("python dashboard.py")
            
    
    
root=Tk()
obj=Login_System(root)
root.mainloop()