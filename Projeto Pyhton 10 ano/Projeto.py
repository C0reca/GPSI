#funções
from Pedra_Papel_Tesoura.mainppt import validppt
from Jogo_Do_Galo.galomain import validgalo
from Admin.admin import validadmin

#apresenta as informações do pograma
def p1():
    print(55*'-'+'Mini Jogos'+55*'-')
    #abre o ficheiro com as informações do pograma
    f=open('Info_Ajuda/info.txt','r')
    print(f.read())
    f.close
    print(120*'-')
    print('Para prosseguir com o pograma carregue enter')
    n=input()

#apresenta o login do pograma
def login():
    print(19*'-','Login',19*'-')
    print('-> 1: Jogador')
    print('-> 2: Admin')
    print('-> 3: Ajuda')
    print('-> 4: Sair')
    op=int(input('Opção: '))
    return op

#valida as opções acima como a pass do admin
def valid():
    while True:
        op=login()
        if op==1:
            validjogo()
        elif op==2:
            #abre o ficheiro que contem a password
            f=open('Admin/password.txt','r')
            print('Para entrar como admin tem de usar a password')
            pas=str(input('Password: '))
            if pas==(f.read()):
                f.close
                validadmin()
            else:
                print('Senha Errada!')
           
        elif op==3:
            #faz o print do ficheiro com a ajuda
            f=open('Info_Ajuda/ajuda.txt','r')
            r=f.readlines()
            for x in range(5):
                print(r[x])
            f.close
        elif op==4:
            break
        else:
            print('Opção inválida!')
            
#mostra todos os jogos que se pode jogar
def jogar():
    print(19*'-','Jogos',19*'-')
    print('1 - Pedra Papel Tesoura')
    print('2 - Jogo do Galo')
    print('3 - Ajuda')
    print('4 - Sair')
    op=int(input('Opção: '))
    return op

#faz a validação do menu dos jogos
def validjogo():
    while True:
        op=jogar()
        if op==1:
            validppt()
        elif op==2:
            validgalo()
        elif op==3:
           #faz o print do ficheiro com a ajuda
            f=open('Info_Ajuda/ajuda.txt','r')
            r=f.readlines()
            for x in range(6,11):
                print(r[x])
            f.close
        elif op==4:
            break
        
    
p1()
valid()
    
