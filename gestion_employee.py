from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import config
from connectDB import  gestionEmployee
from functions1 import utilisateur
gestEmpl = gestionEmployee()

class admin(utilisateur):
    tpl = ()
    def __init__(self):
        utilisateur.__init__(self)
        self.window1 = Tk()
        self.window1.title('gestion employee')
        self.window1.geometry('1000x650')
        self.img1 = PhotoImage(file='logo.png')
        self.window1.iconphoto(False, self.img1)
        self.window1.configure(bg="#262626")
        self.window1.resizable(False, False)
        self.img = PhotoImage(file='icon_logo.png')
        self.logo = Label(self.window1, image=self.img, bg="#262626")
        self.logo.place(x=15, y=14, width=68, height=73)
        self.welcome = Label(self.window1, text=('Welcome , ' + config.username), fg="white",
                             font=('Courier', 12, "bold"),
                             bg="#262626")
        self.welcome.place(x=673, y=41)
        self.logout = Button(self.window1, text="Go Back", borderwidth=0, font=(14), bg="#EC4F1D", fg="white",
                             command=self.logout)
        self.logout.place(x=845, y=38, width=76, height=28)
        self.white_mode = PhotoImage(file='white_mode.png')
        self.dark_mode = PhotoImage(file='dark_mode.png')
        self.state = "black"
        self.change_mode = Button(self.window1, image=self.white_mode, borderwidth=0, font=(14), bg="#292929",
                                  command=self.dark_white_mode,
                                  activebackground="#292929")
        self.change_mode.place(x=949, y=38, width=28, height=28)
        self.Image1 = PhotoImage(file="employe.png")
        self.form = Label(self.window1, image=self.Image1)
        self.form.place(x=32, y=131, width=328, height=474)
        self.nom = Entry(self.form)
        self.nom.place(x=112, y=62, width=200, height=35)
        self.prenom = Entry(self.form)
        self.prenom.place(x=112, y=122, width=200, height=35)
        self.poste = ttk.Combobox(self.form, values=['admin','employee'],state='readonly')
        self.poste.place(x=112, y=182, width=200, height=35)
        self.tele = Entry(self.form)
        self.tele.place(x=112, y=242, width=200, height=35)
        self.username = Entry(self.form)
        self.username.place(x=112, y=302, width=200, height=35)
        self.password = Entry(self.form)
        self.password.place(x=112, y=362, width=200, height=35)
        self.treeView = ttk.Treeview(self.window1)
        self.treeView['columns'] = ('id','nom', 'prenom','poste', 'tele','username','password')
        self.treeView.column('#0', width=0, stretch=NO)
        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['id','nom', 'prenom','poste' , 'tele','username','password']
        for el in self.lst1:
            self.treeView.column(el, anchor=CENTER, width=80)
            self.treeView.heading(el, text=el, anchor=CENTER)
        self.treeView.place(x=395,y=131,width=582,height=474)
        self.scrlbar = ttk.Scrollbar(self.treeView,orient="vertical",command=self.treeView.yview)
        self.scrlbar.pack(side='right', fill='y',ipady=100)
        self.treeView.configure(xscrollcommand=self.scrlbar.set)
        self.ajouter = Button(self.form,text="Ajouter",bg="#3838e2",fg="white",font=('Courier', 11),command = self.inserting)
        self.ajouter.place(x=20,y=421,width=130,height=31)
        self.modifier = Button(self.form, text="Get", bg="#D3D3D3", fg="black", font=('Courier', 11),
                              command=self.modifierEmployee,state= DISABLED)
        self.modifier.place(x=178, y=421, width=130, height=31)
        self.treeView.bind('<ButtonRelease-1>', self.getSelectedUser)
        self.instructions = Label(self.window1,text="Delete - Right click",fg="white",bg="#262626")
        self.instructions.pack(pady=100)
        self.treeView.bind('<Button-3>',self.delete)
        self.getAllValuesBd()
        self.searching = Entry(self.treeView,bg="#D1D1D1")
        self.searching.insert(0,"Saisir username : ")
        self.searching.bind('<Button-1>',lambda event:self.searching.delete(0,END))
        self.searching.pack(side='bottom', fill='x')
        self.searchBtn = Button(self.searching,text="Search",bg="#3838e2",fg="white",width=20,cursor='hand2',command = self.searchEmployee)
        self.searchBtn.pack(side=RIGHT,fill="y")
        self.max = 0
        self.window1.mainloop()
    def getSelectedUser(self,event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="#3838e2", fg="white", state=NORMAL)
    def searchEmployee(self):
        if self.searching.get() != '':
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            lst = gestEmpl.selectUsername(self.searching.get())
            for ele in sorted(lst, key=lambda k: k[0]):
                self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)
        else:
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            self.getAllValuesBd()
    def getAllValuesBd(self):
        lst = gestEmpl.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)
    def returnMax(self):
        lst = gestEmpl.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))
    def getSelectedEmployee(self):
        item = self.treeView.selection()
        lst = []
        if item:
            selected_item = item[0]
            lst = gestEmpl.selectId(selected_item)
        return lst
    def delete(self,event):
        item = self.treeView.selection()
        if item:
            if messagebox.askokcancel("Confirm","Are you sure You wanna delete it ? "):
                    selected_item = item[0]
                    gestEmpl.deleteId(selected_item)
                    self.treeView.delete(selected_item)
                    self.modifier.configure(text='Get', bg="#D3D3D3", fg="black", state=DISABLED)
        else:
            messagebox.showinfo("Warning","Select a row !")

    def dark_white_mode(self):
        if self.state == "black":
            self.window1.configure(bg="white")
            self.welcome.configure(bg="white", fg="#292929")
            self.change_mode.configure(image=self.dark_mode, bg="white", activebackground="white")
            self.logo.configure(bg="white")
            self.state = "white"
        else:
            self.window1.configure(bg="#292929")
            self.welcome.configure(bg="#292929", fg="white")
            self.change_mode.configure(image=self.white_mode, bg="#292929", activebackground="#292929")
            self.logo.configure(bg="#292929")
            self.state = "black"
    def modifierEmployee(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.nom.insert(0,lst[1])
                    self.prenom.insert(0,lst[2])
                    self.poste.insert(0,lst[3])
                    self.tele.insert(0,lst[4])
                    self.password.insert(0,lst[6])
                    self.username.insert(0,lst[5])
                    self.modifier.configure(text='Modifier')
                    self.ajouter.configure(bg="#D3D3D3", fg="black",state=DISABLED)
                else:
                    if self.verif():
                        self.treeView.item(item, values=(lst[0],self.nom.get(),self.prenom.get(),self.poste.get(),self.tele.get(),self.username.get(),self.password.get()))
                        tpl = (self.nom.get(), self.prenom.get(), self.poste.get(), self.tele.get(), self.username.get(),self.password.get(),lst[0])
                        gestEmpl.updateTbl(tpl)
                        self.modifier.configure(text='Get',bg="#D3D3D3", fg="black",state=DISABLED)
                        self.ajouter.configure(bg="#3838e2",fg="white", state=NORMAL)
                        self.emptying()
            except:
                pass
    def emptying(self):
        self.nom.delete(0, END)
        self.prenom.delete(0, END)
        self.poste.delete(0, END)
        self.tele.delete(0, END)
        self.password.delete(0, END)
        self.username.delete(0, END)
    def inserting(self):
        if self.verif():
            self.returnMax()
            i = self.max + 1
            utilisateur.initialize(self,i, self.nom.get(),self.prenom.get(),self.poste.get(),self.tele.get(),self.username.get(), self.password.get())
            tpl = utilisateur.getData(self)
            gestEmpl.insertTbl(tpl)
            self.treeView.insert(parent='', index=i, iid=i, text='h', values=tpl)

            self.emptying()
    def logout(self):
        self.window1.destroy()
        from menu import Menu
        Menu()
    def verif(self):
        if self.nom.get() != '' and self.prenom.get() != '' and self.poste.get() != '' and self.tele.get() != '' and self.password.get() != '' and self.username.get() != '':
            return True
        messagebox.showinfo("warning","can you fill all the inputs !!")
        return False

