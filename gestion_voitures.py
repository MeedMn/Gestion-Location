from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from datetime import date
import config
from functions1 import getImage
from connectDB import  gestVoiture

gv = gestVoiture()
class voiture:
    def __init__(self):
        self.id =''
        self.matricule = ''
        self.marque=''
        self.annee=''
        self.modele=''
        self.carburant=''
        self.prixJour=''
    def initialize(self,id,matricule,marque,annee,modele,carburant,prixJour):
        self.id =id
        self.matricule = matricule
        self.marque=marque
        self.annee=annee
        self.modele=modele
        self.carburant=carburant
        self.prixJour=prixJour
    def getInfosCars(self):
        return self.id,self.matricule,self.marque,self.annee,self.modele,self.carburant,self.prixJour

class admin:
    tpl = ()
    def __init__(self):
        self.window1 = Tk()
        self.window1.title('gestion voitures')
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
        self.Image1 = PhotoImage(file="canva.png")
        self.form = Label(self.window1, image=self.Image1)
        self.form.place(x=32, y=131, width=328, height=474)
        self.Voiture = voiture()
        self.matricule = Entry(self.form)
        self.matricule.place(x=112, y=62, width=200, height=35)
        self.Marque = Entry(self.form)
        self.Marque.place(x=112, y=122, width=200, height=35)
        self.current_year = date.today().year
        self.years = []
        for i in range(1999,self.current_year+1):
            self.years.append(i)
        self.Annee = ttk.Combobox(self.form, values=self.years,state='readonly')
        self.Annee.place(x=112, y=182, width=200, height=35)
        self.Modele = Entry(self.form)
        self.Modele.place(x=112, y=242, width=200, height=35)
        self.Carburant = ttk.Combobox(self.form, values=['essence','gazoile'],state='readonly')
        self.Carburant.place(x=112, y=302, width=200, height=35)
        self.PrixJour = Entry(self.form)
        self.PrixJour.place(x=112, y=362, width=200, height=35)
        self.treeView = ttk.Treeview(self.window1)
        self.treeView['columns'] = ('id','matricule', 'Marque','Annee', 'Modele','Carburant','PrixJour')
        self.treeView.column('#0', width=0, stretch=NO)
        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['id','matricule', 'Marque','Annee' , 'Modele','Carburant','PrixJour']
        for el in self.lst1:
            self.treeView.column(el, anchor=CENTER, width=80)
            self.treeView.heading(el, text=el, anchor=CENTER)
        self.treeView.place(x=395,y=131,width=582,height=474)
        self.scrlbar = ttk.Scrollbar(self.treeView,orient="vertical",command=self.treeView.yview)
        self.scrlbar.pack(side='right', fill='y',ipady=100)
        self.treeView.configure(xscrollcommand=self.scrlbar.set)
        self.ajouter = Button(self.form,text="Ajouter",bg="#3838e2",fg="white",font=('Courier', 11),command = self.insertVoiture)
        self.ajouter.place(x=20,y=421,width=130,height=31)
        self.modifier = Button(self.form, text="Get", bg="#D3D3D3", fg="black", font=('Courier', 11),
                              command=self.modifierVoiture,state= DISABLED)
        self.modifier.place(x=178, y=421, width=130, height=31)
        self.treeView.bind('<ButtonRelease-1>', self.activateGetButton)
        self.instructions = Label(self.window1,text="Delete - Right click    |    Show infos - Double Left Click",fg="white",bg="#262626")
        self.instructions.pack(pady=100)
        self.treeView.bind('<Button-3>',self.delete)
        self.getAllValuesBd()
        self.searching = Entry(self.treeView,bg="#D1D1D1")
        self.searching.insert(0,"Saisir Marque : ")
        self.searching.bind('<Button-1>',lambda event:self.searching.delete(0,END))
        self.searching.pack(side='bottom', fill='x')
        self.searchBtn = Button(self.searching,text="Search",bg="#3838e2",fg="white",width=20,cursor='hand2',command = self.searchVoiture)
        self.searchBtn.pack(side=RIGHT,fill="y")
        self.treeView.bind('<Double-Button-1>',self.showInfoVoiture)
        self.max = 0
        self.window1.mainloop()
    def showInfoVoiture(self,event):
        item = self.treeView.selection()
        if item:
            lst = self.getSelectedCar()
            config.carImg = lst[2]+lst[4]+lst[3]+str(lst[0])
            config.data1 = lst
            self.window1.destroy()
            from carsInfos import carsinfos
            carsinfos()
        else:
            messagebox.showinfo("Warning", "Select a row !")
    def activateGetButton(self,event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="#3838e2", fg="white", state=NORMAL)
    def searchVoiture(self):
        if self.searching.get() != '':
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            lst = gv.selectMarque(self.searching.get())
            for ele in sorted(lst, key=lambda k: k[0]):
                self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)
        else:
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            self.getAllValuesBd()
    def getAllValuesBd(self):
        lst = gv.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            self.treeView.insert(parent='', index=ele[0], iid=ele[0], text='h', values=ele)
    def returnMaxId(self):
        lst = gv.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))
    def getSelectedCar(self):
        item = self.treeView.selection()
        lst = []
        if item:
            selected_item = item[0]
            lst = gv.selectId(selected_item)
        return lst
    def delete(self,event):
        item = self.treeView.selection()
        if item:
            if messagebox.askokcancel("Confirm","Are you sure You wanna delete it ? "):
                    try:
                        import os
                        lst = self.getSelectedCar()
                        os.remove('media/'+lst[2]+lst[4]+lst[3]+str(lst[0])+'.png')
                    except:
                        pass
                    selected_item = item[0]
                    gv.deleteId(selected_item)
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
    def modifierVoiture(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.matricule.insert(0,lst[1])
                    self.Marque.insert(0,lst[2])
                    self.Annee.insert(0,lst[3])
                    self.Modele.insert(0,lst[4])
                    self.PrixJour.insert(0,lst[6])
                    self.Carburant.insert(0,lst[5])
                    self.modifier.configure(text='Modifier')
                    self.ajouter.configure(bg="#D3D3D3", fg="black",state=DISABLED)
                else:
                    if self.verif():
                        self.treeView.item(item, values=(lst[0],self.matricule.get(),self.Marque.get(),self.Annee.get(),self.Modele.get(),self.Carburant.get(),self.PrixJour.get()))
                        tpl = (self.matricule.get(), self.Marque.get(), self.Annee.get(), self.Modele.get(), self.Carburant.get(),self.PrixJour.get(),lst[0])
                        gv.updateTbl(tpl)
                        self.modifier.configure(text='Get',bg="#D3D3D3", fg="black",state=DISABLED)
                        self.ajouter.configure(bg="#3838e2",fg="white", state=NORMAL)
                        self.emptying()
            except:
                pass
    def emptying(self):
        self.matricule.delete(0, END)
        self.Marque.delete(0, END)
        self.Annee.delete(0, END)
        self.Modele.delete(0, END)
        self.PrixJour.delete(0, END)
        self.Carburant.delete(0, END)
    def insertVoiture(self):
        if self.verif():
            self.returnMaxId()
            i = self.max + 1
            self.Voiture.initialize(i, self.matricule.get(),self.Marque.get(),self.Annee.get(),self.Modele.get(),self.Carburant.get(), self.PrixJour.get())
            tpl = self.Voiture.getInfosCars()
            gv.insertTbl(tpl)
            self.treeView.insert(parent='', index=i, iid=i, text='', values=tpl)
            try:
                carImg = self.Voiture.marque + self.Voiture.modele + self.Voiture.annee
                getImage(carImg, i)
            except:
                pass
            self.emptying()
    def logout(self):
        self.window1.destroy()
        from menu import Menu
        Menu()
    def verif(self):
        if self.matricule.get() != '' and self.Marque.get() != '' and self.Annee.get() != '' and self.Modele.get() != '' and self.PrixJour.get() != '' and self.Carburant.get() != '':
            return True
        messagebox.showinfo("warning", "can you fill all the inputs !!")
        return False

