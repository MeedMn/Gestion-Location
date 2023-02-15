from tkinter import *

class facture:
    def __init__(self,data):
        self.factureInfosWindow = Tk()
        self.factureInfosWindow.geometry('1000x650')
        self.factureInfosWindow.title("Facture")
        self.img1 = PhotoImage(file='logo.png')
        self.factureInfosWindow.iconphoto(False, self.img1)
        self.background = PhotoImage(file='facture.png')
        self.label1 = Label(self.factureInfosWindow, image=self.background)
        self.label1.place(x=0, y=0, width=1000, height=650)
        self.factureInfosWindow.resizable(False, False)
        self.logout = Button(self.factureInfosWindow, text="Go Back", borderwidth=0, font=(14), bg="#EC4F1D", fg="white",
                             command=self.logout)
        self.logout.place(x=845, y=38, width=76, height=28)
        (Label(self.factureInfosWindow,text=data[0],font=('Courier', 22,"bold"),bg="#262626",fg="white")).place(x=261,y=240)
        (Label(self.factureInfosWindow,text=data[1][0],font=('Courier', 13,"bold"),bg="#262626",fg="white")).place(x=115,y=118.5)
        (Label(self.factureInfosWindow,text=data[1][1]+' '+data[1][2],font=('Courier', 13,"bold"),bg="#262626",fg="white")).place(x=184,y=139)
        (Label(self.factureInfosWindow,text=data[1][4],font=('Courier', 13,"bold"),bg="#262626",fg="white")).place(x=115,y=157)
        (Label(self.factureInfosWindow,text=data[1][5],font=('Courier', 13,"bold"),bg="#262626",fg="white")).place(x=96,y=176)
        (Label(self.factureInfosWindow, text=data[2][2]+' '+data[2][4]+' '+data[2][3],font=('Courier', 15),bg="#eeeeee",fg="#262626")).place(x=91,y=460)
        (Label(self.factureInfosWindow, text=data[3],font=('Courier', 15),bg="#eeeeee",fg="#262626")).place(x=400,y=460)
        (Label(self.factureInfosWindow, text=data[4],font=('Courier', 15),bg="#eeeeee",fg="#262626")).place(x=595,y=460)
        (Label(self.factureInfosWindow, text=data[2][6],font=('Courier', 15),bg="#eeeeee",fg="#262626")).place(x=825,y=460)
        days = (str(data[4]-data[3])).split()
        (Label(self.factureInfosWindow, text=int(days[0])*int(data[2][6]),font=('Courier', 15),bg="#eeeeee",fg="#262626")).place(x=667,y=602)
        self.factureInfosWindow.mainloop()
    def logout(self):
        self.factureInfosWindow.destroy()
        from Gestion_Location import employee
        employee()