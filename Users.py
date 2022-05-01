from tkinter import*
from turtle import clear, title
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class UsersClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Internet Service Management | Developed By Group 15")
       self.root.config(bg="white")
       self.root.focus_force()
       #=================================
       #All Variables======
       
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()

       self.var_user_id=StringVar()
       self.var_gender=StringVar()
       self.var_phoneNumber=StringVar()
       self.var_name=StringVar()
       self.var_dob=StringVar()
       self.var_dor=StringVar()
       self.var_email=StringVar()
       self.var_pass=StringVar()
       self.var_utype=StringVar()
       self.var_fees=StringVar()


       #=====searchFrame========
       SearchFrame=LabelFrame(self.root,text="Search User",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
       SearchFrame.place(x=250,y=20,width=600,height=70)

       #==options===
       cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Phone","Email"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_search.place(x=10,y=10,width=180)
       cmb_search.current(0)

       txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
       btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

       #=================title===========
       title=Label(self.root,text="Users Detail",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

       #=========content========
       #=========row1===========
       lbl_users_id=Label(self.root,text="Users ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
       lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
       lbl_phoneNumber=Label(self.root,text="Phone",font=("goudy old style",15),bg="white").place(x=750,y=150)

       txt_users_id=Entry(self.root,textvariable=self.var_user_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
       # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
       cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_gender.place(x=500,y=150,width=180)
       cmb_gender.current(0)
       txt_phoneNumber=Entry(self.root,textvariable=self.var_phoneNumber,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

       #====row2=======
       lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
       lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
       lbl_dor=Label(self.root,text="D.O.R",font=("goudy old style",15),bg="white").place(x=750,y=190)

       txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
       txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
       txt_dor=Entry(self.root,textvariable=self.var_dor,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

       #======row3==============
       lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
       lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
       lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)

       txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
       txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
       cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Packet 1", "Packet 2", "Packet 3"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_utype.place(x=850,y=230,width=180)
       cmb_utype.current(0)

       #============row4===========
       lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
       lbl_fees=Label(self.root,text="Fees",font=("goudy old style",15),bg="white").place(x=500,y=270)

       self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.txt_address.place(x=150,y=270,width=300,height=60)
       txt_fees=Entry(self.root,textvariable=self.var_fees,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)

       #====button========
       btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
       btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
       btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

       #====Users Detail====
       users_frame=Frame(self.root,bd=3,relief=RIDGE)
       users_frame.place(x=0,y=350,relwidth=1,height=150)

       scrolly=Scrollbar(users_frame,orient=VERTICAL)
       scrollx=Scrollbar(users_frame,orient=HORIZONTAL)

       self.UsersTable=ttk.Treeview(users_frame,columns=("uid","name","email","gender","phone","dob","dor","pass","utype","address","fees"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.UsersTable.xview)
       scrolly.config(command=self.UsersTable.yview)

       self.UsersTable.heading("uid",text="USER ID")
       self.UsersTable.heading("name",text="Name")
       self.UsersTable.heading("email",text="Email")
       self.UsersTable.heading("gender",text="Gender")
       self.UsersTable.heading("phone",text="Phone")
       self.UsersTable.heading("dob",text="DOB")
       self.UsersTable.heading("dor",text="DOR")
       self.UsersTable.heading("pass",text="Pass")
       self.UsersTable.heading("utype",text="UType")
       self.UsersTable.heading("address",text="Address")
       self.UsersTable.heading("fees",text="Fees")
       
       self.UsersTable["show"]="headings"

       self.UsersTable.column("uid",width=90)
       self.UsersTable.column("name",width=100)
       self.UsersTable.column("email",width=100)
       self.UsersTable.column("gender",width=100)
       self.UsersTable.column("phone",width=100)
       self.UsersTable.column("dob",width=100)
       self.UsersTable.column("dor",width=100)
       self.UsersTable.column("pass",width=100)
       self.UsersTable.column("utype",width=100)
       self.UsersTable.column("address",width=100)
       self.UsersTable.column("fees",width=100)
       self.UsersTable.pack(fill=BOTH,expand=1)
       self.UsersTable.bind("<ButtonRelease-1>",self.get_data)
       
       self.show()
#===================================================================
    def add(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_user_id.get()=="":
                messagebox.showerror("Error","User ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from users where uid =?",(self.var_user_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This User ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into users (uid,name,email,gender,phone,dob,dor,pass,utype,address,fees) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_user_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_phoneNumber.get(),

                                        self.var_dob.get(),
                                        self.var_dor.get(),

                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0', END),
                                        self.var_fees.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Users Add Success",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

    def show(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            cur.execute("select * from users")
            rows=cur.fetchall()
            self.UsersTable.delete(*self.UsersTable.get_children())
            for row in rows:
                self.UsersTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    

    def get_data(self,ev):
        f=self.UsersTable.focus()
        content=(self.UsersTable.item(f))
        row=content['values']
        # print(row)
        self.var_user_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_phoneNumber.set(row[4]),

        self.var_dob.set(row[5]),
        self.var_dor.set(row[6]),

        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_fees.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_user_id.get()=="":
                messagebox.showerror("Error","User ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from users where uid =?",(self.var_user_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid User ID",parent=self.root)
                else:
                    cur.execute("Update users set name=?,email=?,gender=?,phone=?,dob=?,dor=?,pass=?,utype=?,address=?,fees=? where uid=?",(
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_phoneNumber.get(),

                                        self.var_dob.get(),
                                        self.var_dor.get(),

                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_fees.get(),
                                        self.var_user_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Users Updated Success",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

    def delete(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_user_id.get()=="":
                messagebox.showerror("Error","User ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from users where uid =?",(self.var_user_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid User ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from users where uid=?",(self.var_user_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Delete Succes",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def clear(self):
        self.var_user_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_phoneNumber.set(""),

        self.var_dob.set(""),
        self.var_dor.set(""),

        self.var_pass.set(""),
        self.var_utype.set("Package 1"),
        self.txt_address.delete('1.0', END),
        self.var_fees.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select Input should be required",parent=self.root)
            
            else:
                cur.execute("select * from users where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.UsersTable.delete(*self.UsersTable.get_children())
                    for row in rows:
                        self.UsersTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.var_user_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_phoneNumber.set(""),

        self.var_dob.set(""),
        self.var_dor.set(""),

        self.var_pass.set(""),
        self.var_utype.set("Package 1"),
        self.txt_address.insert(""),
        self.var_fees.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

if __name__=="__main__":
    root = Tk()
    obj=UsersClass(root)
    root.mainloop()