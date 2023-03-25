from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

user = StringVar()
pass1 = StringVar()



def database():
    username = user.get()
    password = pass1.get()

    conn = sqlite3.connect('demo')
    with conn:
        cursor = conn.cursor()

    cursor.execute('INSERT INTO login  VALUES(%s,%s)')
    conn.commit()


label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=user)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=pass1)
entry_2.place(x=240, y=180)





Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

root.mainloop()






















