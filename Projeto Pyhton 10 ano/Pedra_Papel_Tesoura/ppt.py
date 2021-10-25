from random import randint


lista = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)

def menu():
    print('Escolha uma opcao para se jogar:') 
    print('0 - Pedra')
    print('1 - Papel')
    print('2 - Tesoura')
    perguntar = int(input('Digite sua escolha: '))
    print("-="*20)
    print("O computador escolheu: {}".format(lista[computador]))
    print("O jogador escolheu: {}".format(lista[perguntar]))
    print("-="*20)
    return perguntar

def valid():
    perguntar=menu()
    if computador == 0:
        if perguntar == 0:
            print("Empate!")
            flag=2
        elif perguntar == 1:
            print("Jogador venceu")
            flag=0
        elif perguntar == 2:
            print("Computador venceu")
            flag=1
        else:
            print("Operacao invalida")

    elif computador == 1:
        if perguntar == 0:
            print("Computador venceu")
            flag=1
        elif perguntar == 1:
            print("Empate!")
            flag=2
        elif perguntar == 2:
            print("Jogador venceu")
            flag=0
        else:
            print("Operacao invalida")
    elif computador == 2:
        if perguntar == 0:
            print("Jogador venceu")
            flag=0
        elif perguntar == 1:
            print("Computador venceu")
            flag=1
        elif perguntar == 2:
            print("Empate!")
            flag=2
        else:
            print("Operacao invalida")
    else:
        print("Operacao invalida")
    return flag

def resultados():
    flag=valid()
    if flag==0:
        f=open('pedra_papel_tesoura/resuljoga.txt','r')
        linha=f.readline()
        f.close
        linha=int(linha)
        linha+=1
        linha=str(linha)
        f=open('pedra_papel_tesoura/resuljoga.txt','w')
        f.write(linha)
        f.close
    if flag==1:
        f=open('pedra_papel_tesoura/resulcomp.txt','r')
        linha=f.readline()
        f.close
        linha=int(linha)
        linha+=1
        linha=str(linha)
        f=open('pedra_papel_tesoura/resulcomp.txt','w')
        f.write(linha)
        f.close

        
        
        
                
                
                
            
                       

