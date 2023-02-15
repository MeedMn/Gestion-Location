from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import config
from connectDB import gestClients, gestionEmployee

gestClient = gestClients()
gestEmpl = gestionEmployee()


class client:
    def __init__(self):
        self.id = ''
        self.nom = ''
        self.prenom = ''
        self.age = ''
        self.email = ''
        self.tele = ''
        self.adresse = ''
        self.id_employee = ''

    def initialize(self, id, nom, prenom, age, email, tele, adresse, id_employee):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email
        self.tele = tele
        self.adresse = adresse
        self.id_employee = id_employee

    def getAllInfos(self):
        return self.id, self.nom, self.prenom, self.age, self.email, self.tele, self.adresse, self.id_employee


class employee:
    tpl = ()

    def __init__(self):
        self.window1 = Tk()
        self.window1.title('Gestion Clients')
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
        self.Image1 = PhotoImage(file="client.png")
        self.form = Label(self.window1, image=self.Image1)
        self.form.place(x=32, y=131, width=328, height=474)
        self.Client = client()
        self.nom = Entry(self.form)
        self.nom.place(x=112, y=62, width=200, height=35)
        self.prenom = Entry(self.form)
        self.prenom.place(x=112, y=122, width=200, height=35)
        self.age = Entry(self.form)
        self.age.place(x=112, y=182, width=200, height=35)
        self.email = Entry(self.form)
        self.email.place(x=112, y=242, width=200, height=35)
        self.tele = Entry(self.form)
        self.tele.place(x=112, y=302, width=200, height=35)
        self.adresse = Entry(self.form)
        self.adresse.place(x=112, y=362, width=200, height=35)
        self.treeView = ttk.Treeview(self.window1)
        self.treeView['columns'] = ('id', 'nom', 'prenom', 'age', 'email', 'tele', 'adresse', 'idEmp')
        self.treeView.column('#0', width=0, stretch=NO)
        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['id', 'nom', 'prenom', 'age', 'email', 'tele', 'adresse', 'idEmp']
        for el in self.lst1:
            self.treeView.column(el, anchor=CENTER, width=70)
            self.treeView.heading(el, text=el, anchor=CENTER)
        self.treeView.place(x=395, y=131, width=582, height=474)
        self.scrlbar = ttk.Scrollbar(self.treeView, orient="vertical", command=self.treeView.yview)
        self.scrlbar.pack(side='right', fill='y', ipady=100)
        self.treeView.configure(xscrollcommand=self.scrlbar.set)
        self.ajouter = Button(self.form, text="Ajouter", bg="#3838e2", fg="white", font=('Courier', 11),
                              command=self.inserting)
        self.ajouter.place(x=20, y=421, width=130, height=31)
        self.modifier = Button(self.form, text="Get", bg="#D3D3D3", fg="black", font=('Courier', 11),
                               command=self.modifierClient, state=DISABLED)
        self.modifier.place(x=178, y=421, width=130, height=31)
        self.treeView.bind('<ButtonRelease-1>', self.activateGetButton)
        self.instructions = Label(self.window1, text="Delete - Right click", fg="white", bg="#262626")
        self.instructions.pack(pady=100)
        self.treeView.bind('<Button-3>', self.delete)
        try:
            self.getAllValuesBdClient()
        except:
            pass
        self.searching = Entry(self.treeView, bg="#D1D1D1")
        self.searching.insert(0, "Saisir nom : ")
        self.searching.bind('<Button-1>', lambda event: self.searching.delete(0, END))
        self.searching.pack(side='bottom', fill='x')
        self.searchBtn = Button(self.searching, text="Search", bg="#3838e2", fg="white", width=20, cursor='hand2',
                                command=self.searchClient)
        self.searchBtn.pack(side=RIGHT, fill="y")
        self.max = 0
        self.window1.mainloop()

    def activateGetButton(self, event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="#3838e2", fg="white", state=NORMAL)

    def searchClient(self):
        if self.searching.get() != '':
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            lst = gestClient.selectNom(self.searching.get())
            for ele in sorted(lst, key=lambda k: k[0]):
                self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)
        else:
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            self.getAllValuesBdClient()

    def getAllValuesBdClient(self):
        lst = gestClient.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)

    def returnMaxid(self):
        lst = gestClient.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))

    def getSelectedClient(self):
        item = self.treeView.selection()
        lst = []
        if item:
            selected_item = item[0]
            lst = gestClient.selectId(selected_item)
        return lst

    def delete(self, event):
        item = self.treeView.selection()
        if item:
            if messagebox.askokcancel("Confirm", "Are you sure You wanna delete it ? "):
                selected_item = item[0]
                gestClient.deleteId(selected_item)
                self.treeView.delete(selected_item)
                self.modifier.configure(text='Get', bg="#D3D3D3", fg="black", state=DISABLED)
        else:
            messagebox.showinfo("Warning", "Select a row !")

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

    def modifierClient(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.nom.insert(0, lst[1])
                    self.prenom.insert(0, lst[2])
                    self.age.insert(0, lst[3])
                    self.email.insert(0, lst[4])
                    self.adresse.insert(0, lst[6])
                    self.tele.insert(0, lst[5])
                    self.modifier.configure(text='Modifier')
                    self.ajouter.configure(bg="#D3D3D3", fg="black", state=DISABLED)
                else:
                    if self.verif():
                        self.treeView.item(item, values=(
                        lst[0], self.nom.get(), self.prenom.get(), self.age.get(), self.email.get(), self.tele.get(),
                        self.adresse.get()))
                        tpl = (self.nom.get(), self.prenom.get(), self.age.get(), self.email.get(), self.tele.get(),
                               self.adresse.get(), lst[0])
                        gestClient.updateTbl(tpl)
                        self.modifier.configure(text='Get', bg="#D3D3D3", fg="black", state=DISABLED)
                        self.ajouter.configure(bg="#3838e2", fg="white", state=NORMAL)
                        self.emptying()
            except:
                pass

    def emptying(self):
        self.nom.delete(0, END)
        self.prenom.delete(0, END)
        self.age.delete(0, END)
        self.email.delete(0, END)
        self.adresse.delete(0, END)
        self.tele.delete(0, END)

    def inserting(self):
        if self.verif():
            self.returnMaxid()
            i = self.max + 1
            self.Client.initialize(i, self.nom.get(), self.prenom.get(), self.age.get(), self.email.get(),
                                   self.tele.get(), self.adresse.get(), gestEmpl.selectUsername(config.username)[0][0])
            tpl = self.Client.getAllInfos()
            gestClient.insertTbl(tpl)
            self.treeView.insert(parent='', index=i, iid=i, text='h', values=tpl)
            self.emptying()

    def logout(self):
        self.window1.destroy()
        from menu import Menu
        Menu()

    def verif(self):
        if self.nom.get() != '' and self.prenom.get() != '' and self.age.get() != '' and self.email.get() != '' and self.adresse.get() != '' and self.tele.get() != '':
            return True
        messagebox.showinfo("warning", "can you fill all the inputs !!")
        return False
