from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.ttk import *

fenetre = Tk()

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)
        fenetre.title('Toolbox')
        self.Labels()
        self.Entry()
        self.Buttons()

    def Labels(self):

        titre_tot = Label(fenetre, text="Calculer un pourcentage")
        titre_tot.grid(row=0, column=0, columnspan=2)

        val_tot = Label(fenetre, text="Valeur totale :")
        val_tot.grid(row=1, column=0)

        val_par = Label(fenetre, text="Valeur partielle :")
        val_par.grid(row=2, column=0)

        res = Label(fenetre, text="Résultat :")
        res.grid(row=3, column=0)

        self.res1 = StringVar()
        res1 = Label(fenetre, textvariable= self.res1)
        res1.grid(row=3, column=1)

        titre_par = Label(fenetre, text="Calculer rune valeur partielle")
        titre_par.grid(row=4, column=0, columnspan=2)

        val_totp = Label(fenetre, text="Valeur totale :")
        val_totp.grid(row=5, column=0)

        val_pourcent = Label(fenetre, text="Pourcentage :")
        val_pourcent.grid(row=6, column=0)

        resp = Label(fenetre, text="Résultat :")
        resp.grid(row=7, column=0)

        self.resp1 = StringVar()
        res2 = Label(fenetre, textvariable=self.resp1)
        res2.grid(row=7, column=1)

    def Entry(self):
        self.SVval_totale = StringVar(value="")
        self.val_totale = Entry(fenetre, width=20, textvariable=self.SVval_totale)
        self.val_totale.grid(row=1, column=1)

        self.SVval_partielle = StringVar(value="")
        self.val_partielle = Entry(fenetre, width=20, textvariable=self.SVval_partielle)
        self.val_partielle.grid(row=2, column=1)

        self.SVval_totalep = StringVar(value="")
        self.val_totalep = Entry(fenetre, width=20, textvariable=self.SVval_totalep)
        self.val_totalep.grid(row=5, column=1)

        self.SVval_pourcent = StringVar(value="")
        self.val_pourcent = Entry(fenetre, width=20, textvariable=self.SVval_pourcent)
        self.val_pourcent.grid(row=6, column=1)

    def Buttons(self):
        choix = Button(fenetre, text="Calculer", command=self.cal_total)
        choix.grid(row=0, column=2, rowspan=4)

        rename = Button(fenetre, text="Calculer", command=self.cal_partiel)
        rename.grid(row=4, column=2, rowspan=4)

    def cal_total(self):
        val_totale = float(self.val_totale.get())
        val_partielle = float(self.val_partielle.get())
        resultat = 100 * (val_partielle / val_totale)
        resultat = round(resultat, 2)
        self.res1.set(resultat)

    def cal_partiel(self):
        val_totale = float(self.val_totalep.get())
        val_pourcent = float(self.val_pourcent.get())
        resultat = (val_pourcent * val_totale) / 100
        resultat = round(resultat, 2)
        self.resp1.set(resultat)


interface = Interface(fenetre)
interface.mainloop()