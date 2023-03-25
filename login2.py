import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

def ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="demo" )
    mycursor = mysqldb.cursor()
    username = e1.get()
    password = e2.get()

    sql= "select * from login where username = %s and password = %s"
    mycursor.execute(sql, [(username), (password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("","Login success")
        root.destroy()
        call(["python", "taskList.py"])

        return True
    else :
        messagebox.showinfo("", "Incorrect username and password")
        return False


def save_info(username, password):
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="demo")
    mycursor = mysqldb.cursor()
    print("connected")

    insert = "INSERT INTO login (username,password) VALUES (%s , %s)"
    values = (username, password)

    try:
        mycursor.execute(insert, values)
        mysqldb.commit()

    except Exception as e:
        print("Was a error " + e)
    mysqldb.close()
    messagebox.showinfo("Data saved sucssefully", username)
    call(["python", "taskList.py"])

root = Tk()
root.title("login")
root.geometry("400x400")
root.config(background='#EFEAD8')
global e1
global e2

title=Label(root, text="WELCOME ",font=('Courier',15),bg='#C18FBA',fg='white')
title.pack(fill=X)

fr1=Frame(root,width='300',height=300,bg='white')
fr1.pack(pady=40)
Label(root, text="Username ",font=('Courier',11),bg='white').place(x=80, y=120)
Label(root, text="Password ",font=('Courier',11),bg='white').place(x=80, y=170)

e1 = Entry(root)
e1.place(x=180, y=120)

e2 = Entry(root)
e2.place(x=180, y=170)
e2.config(show="*")

Button(root, text='Login', command=ok,bg='#EFE2ED',fg='black', height=1,width=13).place(x=90,y=250)
Button(root, text='Sign Up',command=lambda:save_info(e1.get(), e2.get()),bg='#EFE2ED',fg='black', height=1,width=13).place(x=200,y=250)
Label(fr1, text="DEVELOPED BY NORA AND WEHAD ",font=('Courier',10),bg='white').place(x=35,y=260)
root.mainloop()