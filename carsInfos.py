from tkinter import *
import config

class carsinfos:
    def __init__(self):
        self.carinfosWindow = Tk()
        self.carinfosWindow.geometry('1000x650')
        self.carinfosWindow.title("menu")
        self.img1 = PhotoImage(file='logo.png')
        self.carinfosWindow.iconphoto(False, self.img1)
        self.carinfosWindow.configure(bg="#262626")
        self.carinfosWindow.resizable(False, False)
        self.img = PhotoImage(file='icon_logo.png')
        self.logo = Label(self.carinfosWindow, image=self.img, bg="#262626")
        self.logo.place(x=15, y=14, width=68, height=73)
        self.welcome = Label(self.carinfosWindow, text=('Welcome , '+config.username), fg="white", font=('Courier', 12, "bold"),
                      bg="#262626")
        self.welcome.place(x=673, y=41)
        self.logout = Button(self.carinfosWindow, text="Go Back", borderwidth=0, font=(14), bg="#EC4F1D", fg="white", command=self.logout)
        self.logout.place(x=845, y=38, width=76, height=28)
        self.white_mode = PhotoImage(file='white_mode.png')
        self.dark_mode = PhotoImage(file='dark_mode.png')
        self.state = "black"
        self.change_mode = Button(self.carinfosWindow, image=self.white_mode, borderwidth=0, font=(14), bg="#292929", command=self.dark_white_mode,
                             activebackground="#292929")
        self.change_mode.place(x=949, y=38, width=28, height=28)
        self.Image1 = PhotoImage(file="canva.png")
        self.carinfo = Label(self.carinfosWindow,image=self.Image1)
        self.carinfo.place(x=616, y=129, width=328, height=474)
        self.carPicture = PhotoImage(file='avaliable.png')
        try:
            self.carPicture['file'] = 'media/'+config.carImg+'.png'
        except:
            pass
        self.imageHolder = Label(self.carinfosWindow,imag=self.carPicture)
        self.imageHolder.place(x=32,y=129,width=531,height=474)
        self.lst = []
        y = 68.5
        for ele in range(1,7):
            (Label(self.carinfo, text=config.data1[ele], fg="white", bg="#EC4F1D", font=('Courier', 12, "bold"))).place(x=161, y=y)
            y+=59.5
        self.carinfosWindow.mainloop()
    def dark_white_mode(self):
        if self.state == "black":
            self.carinfosWindow.configure(bg="white")
            self.welcome.configure(bg="white", fg="#292929")
            self.change_mode.configure(image=self.dark_mode, bg="white", activebackground="white")
            self.logo.configure(bg="white")
            self.state = "white"
        else:
            self.carinfosWindow.configure(bg="#292929")
            self.welcome.configure(bg="#292929", fg="white")
            self.change_mode.configure(image=self.white_mode, bg="#292929", activebackground="#292929")
            self.logo.configure(bg="#292929")
            self.state = "black"
    def logout(self):
        self.carinfosWindow.destroy()
        from gestion_voitures import admin
        admin()
