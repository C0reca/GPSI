def menu():
    print(10*'-','Admin',10*'-')
    print('1 - Mudar password')
    print('2 - Apagar resultados pedra papel tesoura')
    print('3 - Apagar resultados jogo do galo')
    print('4 - Ajuda')
    print('5 - Sair')
    op=int(input('Opção: '))
    return op

def validadmin():
    while True:
        op=menu()
        if op==1:
            f=open('Admin/password.txt','w')
            f.write(str(input('Nova password: ')))
            f.close
        elif op==2:
            f=open('Pedra_Papel_Tesoura/resulcomp.txt','w')
            f.write('0')
            f.close
            f=open('Pedra_Papel_Tesoura/resuljoga.txt','w')
            f.write('0')
            f.close
        elif op==3:
            f=open('Jogo_Do_Galo/galocomp.txt','w')
            f.write('0')
            f.close
            f=open('Jogo_Do_Galo/galojoga.txt','w')
            f.write('0')
            f.close
        elif op==4:
            #faz o print do ficheiro com a ajuda
            f=open('Info_Ajuda/ajuda.txt','r')
            r=f.readlines()
            for x in range(28,len(r)):
                print(r[x])
            f.close 
        elif op==5:
            break

