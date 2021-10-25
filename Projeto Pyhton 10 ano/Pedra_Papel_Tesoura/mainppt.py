from Pedra_Papel_Tesoura.ppt import resultados

def menu():
    print(10*'-','Pedra Papel Tesoura',10*'-')
    print('1 - Jogar')
    print('2 - Resultados')
    print('3 - Ajudar')
    print('4 - Sair')
    op=int(input('Opção: '))
    return op

def validppt():
    while True:
        op=menu()
        if op==1:
            resultados()
        elif op==2:
            f=open('pedra_papel_tesoura/resuljoga.txt','r')
            linha1=f.readline()
            f.close
            f=open('pedra_papel_tesoura/resulcomp.txt','r')
            linha2=f.readline()
            f.close
            print('Jogador -',linha1)
            print('Computador -',linha2)
        elif op==3:
            #faz o print do ficheiro com a ajuda
            f=open('Info_Ajuda/ajuda.txt','r')
            r=f.readlines()
            for x in range(12,20):
                print(r[x])
            f.close        
        elif op==4:
            break
