from tkinter import *
import tkinter as tk
from function import mysql_registar

def registar():
    app_reg = Tk()
    #mydb=conect()
    app_reg.geometry('600x800')  
    app_reg.title('MyHealth')
    
    def insert():
        username1=username.get()
        password1=password.get()
        nome_completo1=nome_completo.get()
        email1=email.get()
        data_nasc1=data_nasc.get()
        peso_inicial1=peso_inicial.get()
        altura1=altura.get()
        imc1=imc.get()
        exercicio_diario1=exercicio_diario.get()
        calorias1=calorias.get()
        copos_de_agua1=copos_de_agua.get()
        intervalo1=intervalo.get()
        
        print(username1)
        print(nome_completo1)
        print(email1)
        print(data_nasc1)
        print(peso_inicial1)
        print(altura1)
        print(imc1)
        print(exercicio_diario1)
        print(calorias1)
        print(copos_de_agua1)
        print(intervalo1)
 
        mysql_registar(
            username1,
            password1,
            nome_completo1,
            email1,
            data_nasc1,
            peso_inicial1,
            altura1,
            imc1,
            exercicio_diario1,
            calorias1,
            copos_de_agua1,
            intervalo1
        )
        
        


    Label(app_reg, text="User Name",bg='black',fg='white').place(x=10, y=50)
    username = StringVar(app_reg)
    Entry(app_reg, textvariable=username).place(x=10, y=75)
    
    Label(app_reg, text="PassWord",bg='black',fg='white').place(x=10, y=100)
    password = StringVar(app_reg)
    Entry(app_reg, textvariable=password).place(x=10, y=125)

    Label(app_reg, text="Nome Completo",bg='black',fg='white').place(x=10, y=150)
    nome_completo = StringVar(app_reg)
    Entry(app_reg, textvariable=nome_completo).place(x=10, y=175)


    Label(app_reg,text="Email",bg='black',fg='white').place(x=10, y=200)
    email = StringVar(app_reg)
    Entry(app_reg, textvariable=email).place(x=10, y=225)
    

    Label(app_reg,text="Data de Nascimento",bg='black',fg='white').place(x=10, y=250)
    data_nasc = StringVar(app_reg)
    Entry(app_reg, textvariable=data_nasc).place(x=10, y=275)
    

    Label(app_reg,text="Peso",bg='black',fg='white').place(x=10, y=300)
    peso_inicial = StringVar(app_reg)
    Entry(app_reg, textvariable=peso_inicial).place(x=10, y=325)


    Label(app_reg,text="Altura",bg='black',fg='white').place(x=10, y=350)
    altura = StringVar(app_reg)
    Entry(app_reg, textvariable=altura).place(x=10, y=375)
    

    Label(app_reg,text="IMC",bg='black',fg='white').place(x=10, y=450)
    imc = StringVar(app_reg)
    Entry(app_reg, textvariable=imc).place(x=10, y=425)


    Label(app_reg,text="Exercicio Diario",bg='black',fg='white').place(x=10, y=500)
    exercicio_diario = StringVar(app_reg)
    Entry(app_reg, textvariable=exercicio_diario).place(x=10, y=475)
    

    Label(app_reg,text="Calorias",bg='black',fg='white').place(x=10, y=550)
    calorias = StringVar(app_reg)
    Entry(app_reg, textvariable=calorias).place(x=10, y=525)


    Label(app_reg,text="Copos de agua",bg='black',fg='white').place(x=10, y=600)
    copos_de_agua = StringVar(app_reg)
    Entry(app_reg, textvariable=copos_de_agua).place(x=10, y=575)

    Label(app_reg,text="Intervalo",bg='black',fg='white').place(x=10, y=650)
    intervalo = StringVar(app_reg)
    Entry(app_reg, textvariable=intervalo).place(x=10, y=625)

    app_reg.title('MyHealth')
    app_reg.configure(background='black')
    Label(app_reg,text='Criar Utilizador',font=("Arial", 30),bg='black',fg='#74FF00').place(x=10, y=0)

    loginButton = Button(app_reg, text="Criar Utilizador", command=insert,border="0",).place(x=10, y=635)
    loginButton = Button(app_reg, text="Voltar", command=insert,border="0",).place(x=100, y=635)



    
 
    
    app_reg.mainloop()
    


