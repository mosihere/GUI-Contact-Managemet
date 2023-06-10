from tkinter import *
from tkinter import messagebox
from .bl import *



def save_onclick(firstname_var, lastname_var, national_code_var, username_var, password_var, confirm_password_var, form):

    firstname = firstname_var.get()
    lastname = lastname_var.get()
    national_code = national_code_var.get()
    username = username_var.get()
    password = password_var.get()
    confirm_password = confirm_password_var.get()

    res = register_bl(
        firstname=firstname,
        lastname=lastname,
        national_code=national_code,
        username=username,
        password=password,
        confirm_password=confirm_password
    )

    if res[0]=="ERROR":
        messagebox.showerror("Error", res[1])

    if res[0]=="SUCCESS":
        messagebox.showinfo("Success", res[1])

        form.destroy()
        login_form()


def register_form():
    form = Tk()

    form.title("Register page")
    form.geometry("300x500")
    form.resizable(width=False,height=False)
    form.configure(bg="white", padx=15, pady=15)

    firstname_var = StringVar()
    lastname_var = StringVar()
    national_code_var = StringVar()
    username_var = StringVar()
    password_var = StringVar()
    confirm_password_var = StringVar()

    Label(
        master=form, 
        text="Firstname : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=firstname_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white"
    ).pack(side=TOP, fill=X,pady=(0,15))

    Label(
        master=form, 
        text="Lastname : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=lastname_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white"
    ).pack(side=TOP, fill=X,pady=(0,15))

    Label(
        master=form, 
        text="Email : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=national_code_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white"
    ).pack(side=TOP, fill=X,pady=(0,15))
    
    Label(
        master=form, 
        text="Username : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=username_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white"
    ).pack(side=TOP, fill=X,pady=(0,15))

    Label(
        master=form, 
        text="Password : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white" 
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=password_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white",
        show="*"
    ).pack(side=TOP, fill=X,pady=(0,15))

    Label(
        master=form, 
        text="Confirm password : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=confirm_password_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white",
        show="*"
    ).pack(side=TOP, fill=X,pady=(0,15))


    Button(
        master=form,
        text="Register",
        font=("tahoma", 10,"normal"),
        bg="green",
        fg="white",
        pady=5,
        command= lambda: save_onclick(firstname_var, lastname_var, national_code_var, username_var, password_var, confirm_password_var, form)
    ).pack(side=TOP,fill=X, pady=(0,10))

    Button(
        master=form,
        text="Back",
        font=("tahoma", 10,"normal"),
        bg="red",
        fg="white",
        pady=5,
        command= lambda: (form.destroy(), login_form())
    ).pack(side=TOP,fill=X)


    form.mainloop()



def login_onclick(username_var, password_var, form):
    username = username_var.get()
    password = password_var.get()

    res = login_bl(
        username=username,
        password=password
    )

    if res[0]=="ERROR":
        messagebox.showerror("Error", res[1])

    if res[0]=="SUCCESS":
        messagebox.showinfo("Success", res[1])

        form.destroy()
        main_form()


def login_form():
    form = Tk()

    form.title("Login page")
    form.geometry("300x250")
    form.resizable(width=False,height=False)
    form.configure(bg="white", padx=15, pady=15)

    username_var = StringVar()
    password_var = StringVar()

    Label(
        master=form, 
        text="Username : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white"
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=username_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white"
    ).pack(side=TOP, fill=X,pady=(0,15))

    Label(
        master=form, 
        text="Password : ",
        font=("tahoma",10,"bold"),
        anchor=W,
        bg="white" 
    ).pack(side=TOP, fill=X)

    Entry(
        master=form,
        textvariable=password_var,
        border=2,
        font=("tahoma",13,"normal"),
        bg="white",
        show="*"
    ).pack(side=TOP, fill=X,pady=(0,15))


    Button(
        master=form,
        text="Login",
        font=("tahoma", 10,"normal"),
        bg="green",
        fg="white",
        pady=5,
        command= lambda: login_onclick(username_var, password_var, form)
    ).pack(side=TOP,fill=X, pady=(0,10))

    Button(
        master=form,
        text="Register",
        font=("tahoma", 10,"normal"),
        bg="red",
        fg="white",
        pady=5,
        command= lambda: (form.destroy(), register_form())
    ).pack(side=TOP,fill=X)


    form.mainloop()


def main_form():
    form = Tk()

    form.title("Main page")
    form.geometry("300x250")
    form.resizable(width=False,height=False)
    form.configure(bg="white", padx=15, pady=15)

    form.mainloop()