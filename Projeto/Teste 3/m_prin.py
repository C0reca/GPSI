from tkinter import *
import tkinter as tk
from sch_ali import TabelaAli

def createNewWindow():
    app2 = Tk()
    app2.title('MyHealth')
    app2.geometry('500x500')
    loginButton = Button(app2, text="Alimentos", command=TabelaAli).pack()
    app2.mainloop()