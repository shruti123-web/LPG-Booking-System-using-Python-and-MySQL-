from tkinter import *
import tkinter as tk
import mysql.connector
import tkinter.messagebox as mb
import tkinter.messagebox
from PIL import Image, ImageTk
from datetime import datetime
import random


connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="password", database="user")
cursordb = connectiondb.cursor()

def login():
    global r_2
    r_2 = Toplevel(root)
    r_2.title("Account Login for Booking")
    r_2.geometry("450x300")

    global username_verification
    global password_verification
    Label(r_2, text='Enter your Account Details', bd=5,font=('arial', 12, 'bold'), fg="white", bg="grey",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(r_2, text="").pack()
    Label(r_2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(r_2, textvariable=username_verification).pack()
    Label(r_2, text="").pack()
    Label(r_2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(r_2, textvariable=password_verification, show="*").pack()
    Label(r_2, text="").pack()
    Button(r_2, text="Login", bg="grey", fg='white', font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(r_2, text="")
    
def register():
    global r_3
    r_3 = Toplevel(root)
    r_3.title("Register")  
    r_3.geometry("600x650")

    global txtFName   
    global txtLName  
    global txtUId  
    global txtPwd  
    global txtContact   
    global txtCity   
    global txtState 
    
    Label(r_3, text = "Register", bd=15, font = ('arial', 15, 'bold'), bg = "grey", fg = "white", width=600).pack()

    txtFName = StringVar()
    txtLName = StringVar()
    txtUId = StringVar()
    txtPwd = StringVar()
    txtContact = StringVar()  
    txtCity = StringVar() 
    txtState = StringVar()
    
    Label(r_3, text = "Enter FirstName:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable=txtFName).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter LastName:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtLName).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter UserId:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtUId).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter Password:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtPwd).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter Contact No:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtContact).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter City:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtCity).pack()
    Label(r_3, text="").pack()
    Label(r_3, text = "Enter State:", font = ('arial', 12, 'bold'), fg = "grey").pack()
    Entry(r_3, textvariable = txtState).pack()
    Label(r_3, text="").pack()
    btn=Button(r_3, text = "Register", font = ('arial', 15, 'bold'), bg = "grey", fg = "white", command = registeration)
    btn.place(x=250, y=550, width=100)

def registeration():
    fname = txtFName.get() 
    lname = txtLName.get()  
    uid = txtUId.get()
    pwd = txtPwd.get()
    contact_no = txtContact.get() 
    city = txtCity.get()
    state = txtState.get() 
    if fname == "":
        mb.showinfo('Information', "Please Enter Firstname")  
        txtFName.focus_set()  
        return  
    if lname == "":
        mb.showinfo('Information', "Please Enter Lastname")  
        txtLName.focus_set()  
        return  
    if uid == "":
        mb.showinfo('Information', "Please Enter User Id")  
        txtUId.focus_set()  
        return  
    if pwd == "":
        mb.showinfo('Information', "Please Enter Password")  
        txtPwd.focus_set()  
        return  
    if contact_no == "":
        mb.showinfo('Information', "Please Enter Contact Number")  
        txtContact.focus_set()  
        return  
    if city == "":
        mb.showinfo('Information', "Please Enter City Name")  
        txtCity.focus_set()  
        return  
    if state == "":
        mb.showinfo('Information', "Please Enter State Name")  
        txtState.focus_set()  
        return

    query1 = "INSERT INTO userRtable(user,password,fname,lname,city,state,mobileno) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (uid, pwd, fname, lname, city, state, contact_no)
    query2 = "INSERT INTO usertable(username,password) VALUES ('%s','%s');" % (uid, pwd)
    try:
        cursordb.execute(query1) 
        cursordb.execute(query2)
        mb.showinfo('Information', "Data inserted Successfully")
        connectiondb.commit()  
    except:
        mb.showinfo('Information', "Data insertion failed!!!") 

def logged_destroy():
    dbr.destroy()
    r_2.destroy()

def logged_destroy_2():
    b_0.destroy()

def failed_destroy():
    failed_message.destroy()

def Lfail():
    global failed_message
    failed_message = Toplevel(r_2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', font=('arial', 12, 'bold'), command=failed_destroy).pack()


def login_verification():
    user_ver = username_verification.get()
    pass_ver = password_verification.get()
    sql = "select * from usertable where username = %s and password = %s"
    cursordb.execute(sql,[(user_ver),(pass_ver)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            dash_board()
            break
    else:
        Lfail()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        r_0.destroy()
        return

def Book_log():
    global r_0
    r_0 = Toplevel(root)
    r_0.title("Login System")
    r_0.geometry("500x500")
    
    Label(r_0,text='Login System',  bd=20, font=('arial', 20, 'bold'), fg="white", bg="grey",width=300).pack()
    Label(r_0,text="").pack()
    Button(r_0,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), fg="white", bg="grey", command=login).pack()
    Label(r_0,text="").pack()
    Button(r_0,text='Register', height="1",width="20", bd=8, font=('arial', 12, 'bold'), fg="white", bg="grey", command=register).pack()
    Label(r_0,text="").pack()
    Button(r_0,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), fg="white", bg="grey", command=Exit).pack()
    Label(r_0,text="").pack()

def book_cnf():
    prf = ta.get()
    fn = tb.get()
    ln = tc.get()
    gn = td.get()
    ms = te.get()
    dob = tf.get()
    na = tg.get()
    ad = th.get()
    lm = ti.get()
    ci = tj.get()
    st = tk.get()
    di = tl.get()
    ema = tm.get()

    if prf == "":
        mb.showinfo('Information', "Please Select Prefix...")  
        ta.focus_set()  
        return  
    if fn == "":
        mb.showinfo('Information', "Please Enter First Name...")  
        etb.focus_set()  
        return 
    if ln == "":
        mb.showinfo('Information', "Please Enter Last Name...")  
        etc.focus_set()  
        return  
    if gn == "":
        mb.showinfo('Information', "Please Select Gender...")  
        ta.focus_set()  
        return
    if ms == "":
        mb.showinfo('Information', "Please Select Marital Status...")  
        te.focus_set()  
        return  
    if dob == "":
        mb.showinfo('Information', "Please Enter Date Of Birth...")  
        etf.focus_set()  
        return
    if dob == "DD-MM-YYYY":
        mb.showinfo('Information', "Please Enter Date Of Birth...")  
        etf.focus_set()  
        return
    if na == "":
        mb.showinfo('Information', "Please Select Nationality...")  
        tg.focus_set()  
        return  
    if ad == "":
        mb.showinfo('Information', "Please Enter Address...")  
        eth.focus_set()  
        return
    if ci == "":
        mb.showinfo('Information', "Please Enter City...")  
        etj.focus_set()  
        return
    if st == "":
        mb.showinfo('Information', "Please Enter State...")  
        etk.focus_set()  
        return
    if di == "":
        mb.showinfo('Information', "Please Select Distributor...")  
        tl.focus_set()  
        return
    if ema == "":
        mb.showinfo('Information', "Please Enter E-mail...")  
        etm.focus_set()  
        return

    d_obj=datetime.strptime(dob,'%d-%m-%Y').date()
    usern = username_verification.get()
    
    query01 = "INSERT INTO book_detail(prefix, fname, lname, gender, marital_s, d_o_b, nationality, address, landmark, city, state, ditributer, email) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (prf, fn, ln, gn, ms, d_obj, na, ad, lm, ci, st, di, ema)
    query02 = "INSERT INTO book_stat(username, fname, lname, distributor, email) VALUES ('%s','%s','%s','%s','%s');" % (usern, fn, ln, di, ema)
    try:
        cursordb.execute(query01) 
        cursordb.execute(query02)
        mb.showinfo('Information', "LPG Booked Successfully")
        connectiondb.commit()  
    except:
        mb.showinfo('Information', "Unable to Book!!!")

def new_booking():
    global b_0
    b_0 = Toplevel(dbr)
    b_0.title("New Booking")
    b_0.geometry("700x1000")

    Label(b_0, text='NEW LPG BOOKING', bd=20,font=('arial', 20, 'bold'), fg="white", bg="grey",width=300).pack()

    global ta 
    global tb  
    global tc  
    global td
    global te   
    global tf  
    global tg
    global th
    global ti
    global tj
    global tk
    global tl
    global tm
    global eta
    
    ta = StringVar()
    tb = StringVar()
    tc = StringVar()
    td = StringVar()
    te = StringVar()  
    tf = StringVar() 
    tg = StringVar()
    th = StringVar()
    ti = StringVar()
    tj = StringVar()
    tk = StringVar()
    tl = StringVar()
    tm = StringVar()
    
    l_ta=Label(b_0, text = "* PREFIX:", font = ('arial', 12, 'bold'), fg = "grey")
    l_ta.place(x= 150, y = 100)
    prefix=[ 'Ms.' ,'Mr.']
    ta=StringVar()
    droplist=OptionMenu(b_0,ta, *prefix)
    droplist.config(width=15)
    ta.set('Select Prefix')
    droplist.place(x=400,y=100, width=150)
    
    l_tb=Label(b_0, text = "* FIRST NAME:", font = ('arial', 12, 'bold'), fg = "grey")
    l_tb.place(x= 150, y = 140)
    etb=Entry(b_0, textvariable = tb).place(x= 400, y = 140, width = 150)
    
    l_tc=Label(b_0, text = "* LAST NAME:", font = ('arial', 12, 'bold'), fg = "grey")
    l_tc.place(x= 150, y = 180)
    etc=Entry(b_0, textvariable = tc).place(x= 400, y = 180, width = 150)

    l_td=Label(b_0, text = "* GENDER:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 220)
    gen=[ 'Male' ,'Female','Others']
    td=StringVar()
    droplist=OptionMenu(b_0,td, *gen)
    droplist.config(width=15)
    td.set('Select Gender')
    droplist.place(x=400,y=220, width=150)
    
    l_te=Label(b_0, text = "* MARITAL STATUS:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 260)
    mar_sts=[ 'Married' ,'Unmarried' , 'Divorced' ,'Widowed']
    te=StringVar()
    droplist=OptionMenu(b_0,te, *mar_sts)
    droplist.config(width=15)
    te.set('Select Marital Status')
    droplist.place(x=400,y=260, width=150)
    
    l_tf=Label(b_0, text = "* DATE OF BIRTH:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 300)
    tf.set("DD-MM-YYYY")
    etf=Entry(b_0, textvariable = tf).place(x= 400, y = 300, width = 150)
    
    l_tg=Label(b_0, text = "* NATIONALITY:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 340)
    nat=[ 'Indian' ,'Non-Resident Indian']
    tg=StringVar()
    droplist=OptionMenu(b_0,tg, *nat)
    droplist.config(width=15)
    tg.set('Select Nationality')
    droplist.place(x=400,y=340, width=150)
    
    l_th=Label(b_0, text = "* ADDRESS:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 380)
    eth=Entry(b_0, textvariable = th).place(x= 400, y = 380, width = 150)
    
    l_ti=Label(b_0, text = "  LANDMARK:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 420)
    eti=Entry(b_0, textvariable = ti).place(x= 400, y = 420, width = 150)
    
    l_tj=Label(b_0, text = "* CITY/TOWN/VILLAGE:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 460)
    etj=Entry(b_0, textvariable = tj).place(x= 400, y = 460, width = 150)
    
    l_tk=Label(b_0, text = "* STATE:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 500)
    etk=Entry(b_0, textvariable = tk).place(x= 400, y = 500, width = 150)
    
    l_tl=Label(b_0, text = "* DISTRIBUTOR:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 540)
    dist=[ 'National Gas Service' ,'Padma Gas Servies' , 'Chintu Gas Servies' ,'Bharatiya Gas Servies']
    tl=StringVar()
    droplist=OptionMenu(b_0,tl, *dist)
    droplist.config(width=15)
    tl.set('Select Distributor')

    droplist.place(x=400,y=540, width=150)
    
    l_tm=Label(b_0, text = "* E-MAIL:", font = ('arial', 12, 'bold'), fg = "grey").place(x= 150, y = 580)
    etm=Entry(b_0, textvariable = tm).place(x= 400, y = 580, width = 150)
    
    book_btn=Button(b_0, text = "BOOK CYLINDER", font = ('arial', 20, 'bold'), bg = "grey", fg = "white", command = book_cnf)
    book_btn.place(x=75, y= 700, width=250)
    exit_btn=Button(b_0, text = "EXIT", font = ('arial', 20, 'bold'), bg = "grey", fg = "white", command = logged_destroy_2)
    exit_btn.place(x=375, y= 700, width=250)

def view_booking():
    global b_1
    b_1 = Toplevel(dbr)
    b_1.title("View Booking")
    b_1.geometry("600x600")

    Label(b_1, text='VIEW MY BOOKING', bd=20,font=('arial', 20, 'bold'), fg="white", bg="grey",width=300).pack()

    bid = random.randint(1111,9999)
    userna = username_verification.get()

    s1 = "select fname from book_stat where username = %s" 
    s2 = "select lname from book_stat where username = %s" 
    s3 = "select distributor from book_stat where username = %s"

    cursordb.execute(s1, [(userna)])
    re1=cursordb.fetchone()
    cursordb.execute(s2, [(userna)])
    re2=cursordb.fetchone()
    cursordb.execute(s3, [(userna)])
    re3=cursordb.fetchone()

    l_1=Label(b_1, text = "USERNAME", font = ('arial', 12, 'bold'), fg = "grey")
    l_1.place(x= 125, y = 200)
    l_a=Label(b_1, text = ":", font = ('arial', 14, 'bold'), fg = "grey")
    l_a.place(x= 280, y = 200)
    l_2=Label(b_1, text = userna, font = ('arial', 12, 'bold'), fg = "grey")
    l_2.place(x= 325, y = 200)
    l_3=Label(b_1, text = "NAME", font = ('arial', 12, 'bold'), fg = "grey")
    l_3.place(x= 125, y = 250)
    l_b=Label(b_1, text = ":", font = ('arial', 14, 'bold'), fg = "grey")
    l_b.place(x= 280, y = 250)
    for i,j in zip(re1,re2):
        l_4=Label(b_1, text = "%s %s" % (i,j), font = ('arial', 12, 'bold'), fg = "grey")
        l_4.place(x= 325, y = 250)
        break
    l_5=Label(b_1, text = "BOOKING ID", font = ('arial', 12, 'bold'), fg = "grey")
    l_5.place(x= 125, y = 300)
    l_c=Label(b_1, text = ":", font = ('arial', 14, 'bold'), fg = "grey")
    l_c.place(x= 280, y = 300)
    l_6=Label(b_1, text = bid, font = ('arial', 12, 'bold'), fg = "grey")
    l_6.place(x= 325, y = 300)
    l_7=Label(b_1, text = "DISTRIDUTER", font = ('arial', 12, 'bold'), fg = "grey")
    l_7.place(x= 125, y = 350)
    l_d=Label(b_1, text = ":", font = ('arial', 14, 'bold'), fg = "grey")
    l_d.place(x= 280, y = 350)
    l_8=Label(b_1, text = "%s" % re3, font = ('arial', 12, 'bold'), fg = "grey")
    l_8.place(x= 325, y = 350)
    l_9=Label(b_1, text = "BOOKING STATUS", font = ('arial', 12, 'bold'), fg = "grey")
    l_9.place(x= 125, y = 400)
    l_e=Label(b_1, text = ":", font = ('arial', 14, 'bold'), fg = "grey")
    l_e.place(x= 280, y = 400)
    l_10=Label(b_1, text = "Successfully Booked", font = ('arial', 12, 'bold'), fg = "green")
    l_10.place(x= 325, y = 400)
    
def dash_board():
    global dbr
    dbr = Toplevel(r_2)
    dbr.title("Dashboard")
    dbr.geometry("1000x1000")

    user = username_verification.get()
    pas = password_verification.get()
    
    sqlc = "select fname from userRtable where user = %s and password = %s" 
    sqll = "select lname from userRtable where user = %s and password = %s"

    cursordb.execute(sqlc, [(user), (pas)])
    r1=cursordb.fetchone()
    cursordb.execute(sqll, [(user), (pas)])
    r2=cursordb.fetchone()
    for i,j in zip(r1,r2):
        Label(dbr, text="Login Successfully!... Welcome %s %s" % (i, j), fg="green", font="bold").pack()
        Label(dbr, text="").pack()
        break
    
    Label(dbr, text='LPG BOOKING SYSTEM', bd=20,font=('arial', 20, 'bold'), fg="white", bg="grey",width=300).pack()
    
    New_conn=tk.Button(dbr,text='New LPG Booking', height="5",width="400", font=('arial', 17, 'bold'), fg="white", bg="grey", command = new_booking)
    New_conn.place(x=150, y=450, width=300)
    New_booking=tk.Button(dbr,text='View My Bookings', height="5",width="400", font=('arial', 17, 'bold'), fg="white", bg="grey", command = view_booking)
    New_booking.place(x=550, y=450, width=300)

    log_bttn=Button(dbr, text="Logout", bg="grey", fg='white', font=('arial', 15, 'bold'), command = logged_destroy)
    log_bttn.place(x=450, y=700, width=100)
    
    img  = Image.open("E:/lpg.png") 
    photo=ImageTk.PhotoImage(img)
    Label(dbr, image=photo).place(x=250,y=125).pack()
    
def main_display():
    global root
    root = tk.Tk()
    root.title("LPG BOOKING SYSTEM")
    root.geometry("1000x1000")
    
    Label(root, text='LPG BOOKING SYSTEM', bd=20,font=('arial', 20, 'bold'), fg="white", bg="grey",width=300).pack()
    
    New_conn=tk.Button(root,text='New Connection', height="5",width="400", font=('arial', 17, 'bold'), fg="white", bg="grey", command=Book_log)
    New_conn.place(x=150, y=450, width=300)
    New_booking=tk.Button(root,text='New Booking', height="5",width="400", font=('arial', 17, 'bold'), fg="white", bg="grey", command=Book_log)
    New_booking.place(x=550, y=450, width=300)

    img  = Image.open("E:/lpg.png") 
    photo=ImageTk.PhotoImage(img)
    Label(root, image=photo).place(x=250,y=75).pack()
    
main_display()
root.mainloop()
