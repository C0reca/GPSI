from tkinter import messagebox
from conection_bd import conect
from m_prin import createNewWindow

def popup():
  messagebox.showerror(title=None, message="Username ou Password errado",)
  
def insert(username1,password1):
    mydb=conect()
    mycursor = mydb.cursor()
    userlogin=username1
    passwordlogin=password1
    mycursor.execute("SELECT * FROM login")
    result = mycursor.fetchall()
    #Verificar se dados sao validos
    flag=0
    for record in result:
        if userlogin == record[0] and passwordlogin == record[1]:
            flag=1
            break
    mydb.close()
    if flag==1:
        createNewWindow()
    else:
        popup()
        
def mysql_registar(username1,
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
                   intervalo1):
    mydb=conect()
    mycursor = mydb.cursor()
    username=username1
    passw=password1
    nome_completo=nome_completo1
    email=email1
    data_nasc=data_nasc1
    peso_inicial=peso_inicial1
    altura=altura1
    imc=imc1
    exercicio_diario=exercicio_diario1
    calorias=calorias1
    copos_de_agua=copos_de_agua1
    intervalo=intervalo1

    print('-------------')
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
    print('-------------')
    print(username)
    print('-------------')
    print(nome_completo)
    print(email)
    print(data_nasc)
    print(peso_inicial)
    print(altura)
    print(imc)
    print(exercicio_diario)
    print(calorias)
    print(copos_de_agua)
    print(intervalo)

    sql = "INSERT INTO login (username_cli,password) VALUES (%s, %s)"
    val = (username,passw)
    mycursor.execute(sql, val)
    
    sql1 = "INSERT INTO clientes ( `username_cli`, `nome_completo`, `email`, `data_nasc`, `peso_incial`, `altura`, `imc`, `exercicio_diario`, `calorias`, `copos_de_agua`, `intervalo`)  VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val1 = (username,
            nome_completo,
            email,
            data_nasc,
            peso_inicial,
            altura,
            imc,
            exercicio_diario,
            calorias,
            copos_de_agua,
            intervalo)
    
    mycursor.execute(sql1, val1)

    mydb.commit()