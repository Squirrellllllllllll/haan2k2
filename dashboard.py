import os
from time import time
from tkinter import*
from PIL import Image,ImageTk
from Users import UsersClass
from package import packageClass
import time
class ISM:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Internet Service Management | Developed By Group 15")
        self.root.config(bg="white")
        #===title=====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Internet Service Management",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===clock====
        self.lbl_clock=Label(self.root,text="Welcome to Internet Service Management\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Left_Menu=====
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("time new romans",20),bg="#009688").pack(side=TOP,fill=X)
        btn_Package=Button(LeftMenu,text="Package",command=self.package,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new romans",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Users=Button(LeftMenu,text="Users",command=self.Users,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new romans",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #====content====
        self.lbl_users=Label(self.root,text="Total Users\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_users.place(x=300,y=120,height=150,width=300)
        
        self.lbl_packet1=Label(self.root,text="Total Packet 1\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_packet1.place(x=650,y=120,height=150,width=300)
        
        self.lbl_packet2=Label(self.root,text="Total Packet 2\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_packet2.place(x=1000,y=120,height=150,width=300)

        self.lbl_packet3=Label(self.root,text="Total Packet 3\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_packet3.place(x=300,y=300,height=150,width=300)
        #===footer====
        lbl_footer=Label(self.root,text="ISM-Internet Service Management | Developed By Group 15\nFor any Contact: 0989999999",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_date_time()
    #===========================================================================================================

    def Users(self):
        self.new__win=Toplevel(self.root)
        self.new__obj=UsersClass(self.new__win)
        
    def package(self):
        self.new__win=Toplevel(self.root)
        self.new__obj=packageClass(self.new__win)
        
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d:%m:%Y")
        self.lbl_clock.config(text=f"Welcome to Internet Service Management\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root = Tk()
    obj=ISM(root)
    root.mainloop()