from tkinter import *
import tkinter as tk
from tab_ali import listar_alimentos

def TabelaAli():
    app1 = Tk()
    app1.geometry('500x500')
    app1.title('MyHealth')
    
    Label(app1, text="Pesquisar Alimento",bg='black',fg='white').place(x=10, y=50)
    alimento1 = StringVar()
    Entry(app1, textvariable=alimento1).place(x=10, y=75)
    
    def l_a():
        alimento=alimento1.get()
        listar_alimentos(alimento)

    tt = Button(app1, text="Pesquisar", command=l_a,border="0",).pack()