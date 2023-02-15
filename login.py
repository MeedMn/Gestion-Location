from tkinter import *
from tkinter import messagebox
import config
from menu import Menu
from connectDB import gestionEmployee,createTables
createTables()
gestiEmpl = gestionEmployee()
class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry('700x450')
        self.img = PhotoImage(file='logo.png')
        self.window.iconphoto(False, self.img)
        self.window.configure(bg="#4169E1")
        self.window.resizable(False, False)
        self.background = PhotoImage(file='img.png')
        self.label1 = Label(self.window, image=self.background)
        self.label1.place(x=0, y=0, width=700, height=450)
        self.label2 = Label(self.window, image=self.img, bg="#262626")
        self.label2.place(x=457, y=22, width=130, height=140)
        self.label3 = Label(self.window, text="username", fg="white", font=('Courier', 12, "bold"), bg="#262626")
        self.label3.place(x=484, y=160)
        self.label4 = Label(self.window, text="password", fg="white", font=('Courier', 12, "bold"), bg="#262626")
        self.label4.place(x=484, y=240)
        self.e1 = Entry(self.window)
        self.e1.place(x=426, y=186, width=200, height=30)
        self.e2 = Entry(self.window, show="*")
        self.e2.place(x=426, y=266, width=200, height=30)
        self.btn = Button(self.window, text="Login", borderwidth=0, font=(4, 10, "bold"), bg="#EC4F1D", fg="white",command=self.button_clicked)
        self.btn.place(x=426, y=326, width=200, height=30)
        self.tentative = 0
        self.acc = False
        self.window.mainloop()
    def button_clicked(self):
        username = self.e1.get()
        password = self.e2.get()

        if username != '' and password != '':
            for ele in gestiEmpl.selectALL():
                if username == ele[5] and password == ele[6]:
                    config.username = username
                    config.role = ele[3]
                    self.window.destroy()
                    self.acc = True
                    Menu()
            if not self.acc:
                messagebox.showinfo("Warning","Verify your username or password")
                self.tentative+=1
        else:
            messagebox.showinfo("Warining","Enter username and password")
        if self.tentative == 3:
            messagebox.showinfo("Warning","You tried this 3 times")
            self.window.destroy()

if __name__ == "__main__":
    Login()