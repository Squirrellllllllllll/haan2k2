from tkinter import*
from turtle import title
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class packageClass:
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

       self.var_pack_invoice=StringVar()
       self.var_pack_name=StringVar()
       self.var_capacity=StringVar()


       #=====Search========
       #==options===
       lbl_search=Label(self.root,text="Packet No.",bg="white",font=("goudy old style",15))
       lbl_search.place(x=700,y=80)

       txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=160)
       btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

       #=================title===========
       title=Label(self.root,text="Package Detail",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

       #=========content========
       #=========row1===========
       lbl_pack_invoice=Label(self.root,text="Package No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
       txt_pack_invoice=Entry(self.root,textvariable=self.var_pack_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
       

       #====row2=======
       lbl_pack_name=Label(self.root,text="Pg.Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
       txt_pack_name=Entry(self.root,textvariable=self.var_pack_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)

       #======row3==============
       lbl_capacity=Label(self.root,text="Capacity",font=("goudy old style",15),bg="white").place(x=50,y=160)
       txt_capacity=Entry(self.root,textvariable=self.var_capacity,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
       
       #============row4===========
       lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
       self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.txt_desc.place(x=180,y=200,width=470,height=120)

       #====button========
       btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
       btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
       btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
       btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

       #====Users Detail====
       users_frame=Frame(self.root,bd=3,relief=RIDGE)
       users_frame.place(x=700,y=120,width=380,height=350)

       scrolly=Scrollbar(users_frame,orient=VERTICAL)
       scrollx=Scrollbar(users_frame,orient=HORIZONTAL)

       self.packageTable=ttk.Treeview(users_frame,columns=("invoice","pack_name","capicity","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.packageTable.xview)
       scrolly.config(command=self.packageTable.yview)

       self.packageTable.heading("invoice",text="Package No.")
       self.packageTable.heading("pack_name",text="Pack Name")
       self.packageTable.heading("capicity",text="Capicity")
       self.packageTable.heading("desc",text="Description")
       self.packageTable["show"]="headings"
       self.packageTable.column("invoice",width=90)
       self.packageTable.column("pack_name",width=100)
       self.packageTable.column("capicity",width=100)
       self.packageTable.column("desc",width=100)
       self.packageTable.pack(fill=BOTH,expand=1)
       self.packageTable.bind("<ButtonRelease-1>",self.get_data)
       
       self.show()
#===================================================================
    def add(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_pack_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from package where invoice=?",(self.var_pack_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into package(invoice,pack_name,capicity,desc) values(?,?,?,?)",(
                                        self.var_pack_invoice.get(),
                                        self.var_pack_name.get(),
                                        self.var_capacity.get(),
                                        self.txt_desc.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Package Add Success",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

    def show(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            cur.execute("select * from package")
            rows=cur.fetchall()
            self.packageTable.delete(*self.packageTable.get_children())
            for row in rows:
                self.packageTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    

    def get_data(self,ev):
        f=self.packageTable.focus()
        content=(self.packageTable.item(f))
        row=content['values']
        # print(row)
        self.var_pack_invoice.set(row[0]),
        self.var_pack_name.set(row[1]),
        self.var_capacity.set(row[2]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3])

    def update(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_pack_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from package where invoice =?",(self.var_pack_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    cur.execute("Update package set pack_name=?,capicity=?,desc=? where invoice=?",(
                                        self.var_pack_name.get(),
                                        self.var_capacity.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_pack_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Package Updated Success",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

    def delete(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_pack_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from package where invoice =?",(self.var_pack_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from package where invoice=?",(self.var_pack_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Package delete Succes",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def clear(self):
        self.var_pack_invoice.set(""),
        self.var_pack_name.set(""),
        self.var_capacity.set(""),
        self.txt_desc.delete('1.0', END),
        self.var_searchtxt.set(""),
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ism.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select * from package where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.packageTable.delete(*self.packageTable.get_children())
                    self.packageTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj=packageClass(root)
    root.mainloop()