import random as ran


# Feito por zzAlfa / Versão 2.0


# Printador do jogo
def printlista(listai):
    listacopy = listai.copy()
    for c in range(0, len(listacopy)):
        if listacopy[c] == '(X)':
            listacopy[c] = '\033[31m' + listacopy[c] + '\033[0;0m'
        elif listacopy[c] == '(O)':
            listacopy[c] = '\033[33m' + listacopy[c] + '\033[0;0m'
    print('#' * 15)
    print(f'{listacopy[0]} {listacopy[1]} {listacopy[2]}')
    print(f'{listacopy[3]} {listacopy[4]} {listacopy[5]}')
    print(f'{listacopy[6]} {listacopy[7]} {listacopy[8]}')
    print('#' * 15)


# Função para checar se alguém venceu (Compara se o playerOne venceu em relação ao playerTwo)
def checkwin(lista, player1, player2):
    if f'({player1})' == lista[0] == lista[1] == lista[2] or f'({player1})' == lista[3] == lista[4] == lista[5] \
            or f'({player1})' == lista[6] == lista[7] == lista[8]:
        resu = 'win'
        onde = 'horizontal' 
        return resu, onde
    elif f'({player1})' == lista[0] == lista[3] == lista[6] or f'({player1})' == lista[1] == lista[4] == lista[7] \
            or f'({player1})' == lista[2] == lista[5] == lista[8]:
        resu = 'win'
        onde = 'vertical'
        return resu, onde
    elif f'({player1})' == lista[0] == lista[4] == lista[8] or f'({player1})' == lista[6] == lista[4] == lista[2]:
        resu = 'win'
        onde = 'diagonal'
        return resu, onde
    else:
        if f'({player2})' == lista[0] == lista[1] == lista[2] or f'({player2})' == lista[3] == lista[4] == lista[5] \
                or f'({player2})' == lista[6] == lista[7] == lista[8]:
            resu = 'lost'
            onde = 'horizontal'
            return resu, onde
        elif f'({player2})' == lista[0] == lista[3] == lista[6] or f'({player2})' == lista[1] == lista[4] == lista[7] \
                or f'({player2})' == lista[2] == lista[5] == lista[8]:
            resu = 'lost'
            onde = 'vertical'
            return resu, onde
        elif f'({player2})' == lista[0] == lista[4] == lista[8] or f'({player2})' == lista[6] == lista[4] == lista[2]:
            resu = 'lost'
            onde = 'diagonal'
            return resu, onde
        else:
            for c in lista:
                if c != '(X)' and c != '(O)':
                    return 'continua'
            return 'O jogo deu Velha'


# Função que faz a jogada do jogador tipo (X ou O)
def play(lista, choice, tipo):
    while True:
        # Verifica se a posição já foi jogada antes e valida a entrada
        try:
            if int(choice) > 0:
                choice = int(choice) - 1
                if lista[choice] != '(O)' and lista[choice] != '(X)':
                    lista.pop(choice)
                    lista.insert(choice, f'({tipo})')
                    break
            choice = input('Tente escolher outra posição, essa já foi escolhida')

        except IndexError:
            choice = input("Erro! Tente escolher uma posição válida. De 1 a 9")
        except ValueError:
            choice = input("Erro! Você digitou um caractere, tente um número entre 1 e 9 ")


# Função que simula a jogada do computador
def playpc(lista, tipo):
    position = ran.randint(0, 8)
    while True:
        if tipo == 'X':
            if lista[position] != '(O)' and lista[position] != '(X)':
                lista.pop(position)
                lista.insert(position, '(X)')
                break
            else:
                position = ran.randint(0, 8)
        elif tipo == 'O':
            if lista[position] != '(X)' and lista[position] != '(O)':
                lista.pop(position)
                lista.insert(position, '(O)')
                break
            else:
                position = ran.randint(0, 8)
