import tkinter as tk
from tkinter import *
import config

class Menu:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1000x650')
        self.window.title("menu")
        self.img1 = PhotoImage(file='logo.png')
        self.window.iconphoto(False, self.img1)
        self.window.configure(bg="#262626")
        self.window.resizable(False, False)
        self.img = PhotoImage(file='icon_logo.png')
        self.logo = Label(self.window, image=self.img, bg="#262626")
        self.logo.place(x=15, y=14, width=68, height=73)
        self.welcome = Label(self.window, text=('Welcome , ' + config.username), fg="white", font=('Courier', 12, "bold"),
                      bg="#262626")
        self.welcome.place(x=673, y=41)
        self.logout = Button(self.window, text="Logout", borderwidth=0, font=(14), bg="#EC4F1D", fg="white", command=self.logout)
        self.logout.place(x=845, y=38, width=76, height=28)
        self.white_mode = PhotoImage(file='white_mode.png')
        self.dark_mode = PhotoImage(file='dark_mode.png')
        self.state = "black"
        self.change_mode = Button(self.window, image=self.white_mode, borderwidth=0, font=(14), bg="#292929", command=self.dark_white_mode,
                             activebackground="#292929")
        self.change_mode.place(x=949, y=38, width=28, height=28)
        if config.role == "admin":
            self.block1 = "GESTION DES EMPLOYÉS"
            self.block2 = "GESTION DES VOITURES"
        else:
            self.block1 = "GESTION DES CLIENTS"
            self.block2 = "GESTION DES LOCATIONS"
        self.block1_btn = Button(self.window, text=self.block1, borderwidth=0, font=("Courier", 20, "bold"), bg="#EC4F1D", fg="white",
                            activebackground="white", activeforeground="#292929",command=self.btn1GoTo)
        self.block1_btn.place(x=30, y=170, width=446, height=310)
        self.block2_btn = Button(self.window, text=self.block2, borderwidth=0, font=("Courier", 20, "bold"), bg="#EC4F1D", fg="white",
                            activebackground="white", activeforeground="#292929",command=self.btn2GoTo)
        self.block2_btn.place(x=524, y=170, width=446, height=310)
        self.window.mainloop()
    def dark_white_mode(self):
        if self.state == "black":
            self.window.configure(bg="white")
            self.welcome.configure(bg="white", fg="#292929")
            self.change_mode.configure(image=self.dark_mode, bg="white", activebackground="white")
            self.logo.configure(bg="white")
            self.block1_btn.configure(fg="#292929", activebackground="#292929", activeforeground="white")
            self.block2_btn.configure(fg="#292929", activebackground="#292929", activeforeground="white")
            self.state = "white"
        else:
            self.window.configure(bg="#292929")
            self.welcome.configure(bg="#292929", fg="white")
            self.change_mode.configure(image=self.white_mode, bg="#292929", activebackground="#292929")
            self.logo.configure(bg="#292929")
            self.state = "black"
            self.block1_btn.configure(fg="white", activebackground="white", activeforeground="#292929")
            self.block2_btn.configure(fg="white", activebackground="white", activeforeground="#292929")
    def logout(self):
        self.window.destroy()
        from login import Login
        Login()
    def btn2GoTo(self):
        self.window.destroy()
        if self.block2 == "GESTION DES VOITURES":
            from gestion_voitures import admin
            admin()
        if self.block2 == "GESTION DES LOCATIONS":
            from Gestion_Location import employee
            employee()
    def btn1GoTo(self):
        self.window.destroy()
        if self.block1 == "GESTION DES CLIENTS":
            from gestion_clients import employee
            employee()
        if self.block1 == "GESTION DES EMPLOYÉS":
            from gestion_employee import admin
            admin()
