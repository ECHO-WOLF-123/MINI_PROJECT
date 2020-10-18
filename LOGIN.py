from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Passport Application")

frame = LabelFrame(root, padx=100, pady=100)
frame.grid(padx=300, pady=125)

# User-Name Index 
UserName_label = Label(frame, text="    Name:*", padx=2, pady=5).grid(row=0,column=0, padx=1, pady=5)
E = Entry(frame, width=50, borderwidth=3)
E.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

# Password_Index
Password_label = Label(frame, text="Password:*", padx=2, pady=5).grid(row=1,column=0, padx=1, pady=5)
E1 = Entry(frame, width=50, borderwidth=3, show="*")
E1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# BUTTONS -Submit & -New_User
Submit_Button = Button(frame, text=" SUBMIT ", padx=10, pady=5, borderwidth=4)
Submit_Button.grid(row=2, column=2, padx=30, pady=30) 


New_User_Button = Button(frame, text=" New User ", padx=5, pady=5, borderwidth=4)
New_User_Button.grid(row=2, column=3, padx=30, pady=30) 

root.mainloop()
