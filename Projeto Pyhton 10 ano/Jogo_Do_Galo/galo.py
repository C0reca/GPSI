
import random
import os
from time import sleep

def galo():
        t = ['.' for _ in range(9)]

        def ver(jog):
                if t[0] == t[1] == t[2] == jog: return jog
                if t[3] == t[4] == t[5] == jog: return jog
                if t[6] == t[7] == t[8] == jog: return jog
                if t[0] == t[3] == t[6] == jog: return jog
                if t[1] == t[4] == t[7] == jog: return jog
                if t[2] == t[5] == t[8] == jog: return jog
                if t[0] == t[4] == t[8] == jog: return jog
                if t[2] == t[4] ==t [6] == jog: return jog

                return '.'


        def joga():
                l=[]
                for i,v in enumerate(t):
                        if v == '.': l.append(i)

                pos = random.choice(l)
                t[pos] = 'O'
                return pos+1


        def display():
                print(' %s %s %s \n %s %s %s \n %s %s %s\n' % tuple(t))

        Flag = random.randrange(2)

        while True:

                os.system('clear')
                display()
                
                if Flag:
                        while True:
                                x = int(input('Posição user: '))-1
                                if t[x] != '.':
                                        print('Posição já ocupada')
                                else :
                                        t[x] = 'X'
                                        break

                else:
                        print('Posição Pc: %i' % joga())
                        sleep(3)

                display()

                if ver('X') == 'X':
                        print('O Usuário Ganhou')
                        f=open('Jogo_Do_Galo/galojoga.txt','r')
                        linha=f.readline()
                        f.close
                        linha=int(linha)
                        linha+=1
                        linha=str(linha)
                        f=open('Jogo_Do_Galo/galojoga.txt','w')
                        f.write(linha)
                        f.close
                        break

                elif ver('O') == 'O':
                        print('O Computador Ganhou')
                        f=open('Jogo_Do_Galo/galocomp.txt','r')
                        linha=f.readline()
                        f.close
                        linha=int(linha)
                        linha+=1
                        linha=str(linha)
                        f=open('Jogo_Do_Galo/galocomp.txt','w')
                        f.write(linha)
                        f.close
                        break

                elif '.' not in t:
                        print('Empatou...')
                        break


                Flag = not Flag

        print('\nFim de Jogo')
