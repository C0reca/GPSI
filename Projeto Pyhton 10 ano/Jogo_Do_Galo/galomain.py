from Jogo_Do_Galo.galo import galo

def menu():
    print(10*'-','Jogo do Galo',10*'-')
    print('1 - Jogar')
    print('2 - Resultados')
    print('3 - Ajuda')
    print('4 - Sair')
    op=int(input('Opção: '))
    return op

def validgalo():
    while True:
        op=menu()
        if op==1:
            galo()
        elif op==2:
            f=open('Jogo_Do_Galo/galojoga.txt','r')
            linha1=f.readline()
            f.close
            f=open('Jogo_Do_Galo/galocomp.txt','r')
            linha2=f.readline()
            f.close
            print('Jogador -',linha1)
            print('Computador -',linha2)
        elif op==3:
            #faz o print do ficheiro com a ajuda
            f=open('Info_Ajuda/ajuda.txt','r')
            r=f.readlines()
            for x in range(21,28):
                print(r[x])
            f.close        
        elif op==4:
            break
