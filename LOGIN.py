from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def loginmessage():
    messagebox.showinfo("Login", "Login Sucessful")
    

def Frame_Login():
    root = Tk()
    root.title("Passport Application")
    root.iconbitmap("D:/GIT_PROJECT/MINI_PROJECT/images/ico/flight.ico")
    img = ImageTk.PhotoImage(Image.open("D:/GIT_PROJECT/MINI_PROJECT/images/flight.png"))
    my_img = Label(image=img).grid()

    frame = LabelFrame(root, padx=50, pady=150)
    frame.grid(padx=200, pady=110)

    # User-Name Index 
    UserName_label = Label(frame, text="UserName:*", padx=2, pady=5).grid(row=0,column=0, padx=1, pady=5)
    E = Entry(frame, width=50, borderwidth=3)
    E.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

    # Password_Index
    Password_label = Label(frame, text="Password:*", padx=2, pady=5).grid(row=1,column=0, padx=1, pady=5)
    E1 = Entry(frame, width=50, borderwidth=3, show="*")
    E1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # BUTTONS -Submit & -New_User
    Submit_Button = Button(frame, text=" SUBMIT ", padx=10, pady=5, borderwidth=4, command=loginmessage)
    Submit_Button.grid(row=2, column=2, padx=30, pady=30) 

    New_User_Button = Button(frame, text=" New User ", padx=5, pady=5, borderwidth=4)
    New_User_Button.grid(row=2, column=3, padx=30, pady=30) 
    
    root.mainloop()
    
Frame_Login()   # Calling the Frame_Login function
