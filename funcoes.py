import random as ran


# Feito por zzAlfa / Versão 1.0

def listaatual(listai):
    print('#' * 15)
    print(f'{listai[0]} {listai[1]} {listai[2]}')
    print(f'{listai[3]} {listai[4]} {listai[5]}')
    print(f'{listai[6]} {listai[7]} {listai[8]}')
    print('#' * 15)


def checkwin(lista, esc, pc):
    if f'({esc})' == lista[0] == lista[1] == lista[2] or f'({esc})' == lista[3] == lista[4] == lista[5] or f'({esc})' == \
            lista[7] == lista[7] == lista[8]:
        resu = 'win'
        onde = 'horizontal'
        return resu, onde
    elif f'({esc})' == lista[0] == lista[3] == lista[6] or f'({esc})' == lista[1] == lista[4] == lista[7] or f'({esc})' == lista[2] == lista[5] == lista[8]:
        resu = 'win'
        onde = 'vertical'
        return resu, onde
    elif f'({esc})' == lista[0] == lista[4] == lista[8] or f'({esc})' == lista[6] == lista[4] == lista[2]:
        resu = 'win'
        onde = 'diagonal'
        return resu, onde
    else:
        if f'({pc})' == lista[0] == lista[1] == lista[2] or f'({pc})' == lista[3] == lista[4] == lista[5] or f'({pc})' == lista[7] == lista[7] == lista[8]:
            resu = 'lost'
            onde = 'horizontal'
            return resu, onde
        elif f'({pc})' == lista[0] == lista[3] == lista[6] or f'({pc})' == lista[1] == lista[4] == lista[7] or f'({pc})' == lista[2] == lista[5] == lista[8]:
            resu = 'lost'
            onde = 'vertical'
            return resu, onde
        elif f'({pc})' == lista[0] == lista[4] == lista[8] or f'({pc})' == lista[6] == lista[4] == lista[2]:
            resu = 'lost'
            onde = 'diagonal'
            return resu, onde
        else:
            cont = 0
            while cont <= len(lista) - 1:
                if lista[cont] == '( )':
                    cont = 9
                    return 'O jogo ainda não terminou'
                elif cont == len(lista) - 1:
                    cont = 9
                    return 'O jogo deu Velha'
                cont += 1


def play(listap, choice, tipo):
    while True:
        if tipo == 'X':
            if listap[choice] == '( )':
                listap.pop(choice)
                listap.insert(choice, '(X)')
                break
            else:
                choice = int(input('Tente escolher outra posição, essa já foi escolhida por outro jogador '))
        elif tipo == 'O':
            if listap[choice] == '( )':
                listap.pop(choice)
                listap.insert(choice, '(O)')
                break
            else:
                choice = int(input('Tente escolher outra posição, essa já foi escolhida por outro jogador '))


def playpc(listap, tipo):
    posi = ran.randint(0, 8)
    while True:
        if tipo == 'X':
            if listap[posi] == '( )':
                listap.pop(posi)
                listap.insert(posi, '(X)')
                break
            else:
                posi = ran.randint(0, 8)
        elif tipo == 'O':
            if listap[posi] == '( )':
                listap.pop(posi)
                listap.insert(posi, '(O)')
                break
            else:
                posi = ran.randint(0, 8)
