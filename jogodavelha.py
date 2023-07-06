import funcoes as funv

# Feito por zzAlfa / Versão 2.0

inicial = ['(1)', '(2)', '(3)',
           '(4)', '(5)', '(6)',
           '(7)', '(8)', '(9)'
           ]
print('Bem vindo ao Jogo da Velha')
funv.printlista(inicial)
# Recebe a escolha do jogador (X ou O) e valida
while True:
    playerOne = input('Qual você escolhe? X ou O ').upper()
    if playerOne == 'X':
        print(f'Você escolheu {playerOne}')
        playerTwo = 'O'
        break
    elif playerOne == 'O':
        print(f"Você escolheu {playerOne}")
        playerTwo = 'X'
        break
    else:
        print('Tente novamente, sua escolha não foi válida.')
        print('Tente digitar "X" ou "O"')
        print('')
# Recebe a escolha do modo de jogo e valida
while True:
    modo = input('Você irá jogar sozinho ou como outro jogador local? [Solo/Local] ').lower()
    if modo == 'solo':
        print('Você escolheu jogar Solo!')
        break
    elif modo == 'local':
        print('Você escolheu jogar Local!')
        break
    else:
        print('Tente novamente, sua escolha não foi válida.')
        print('Tente digitar "solo" ou "local"')
        print('')

# Modo de jogo solo
if modo == 'solo':
    print('\nO JOGO IRÁ COMEÇAR')
    funv.printlista(inicial)
    if playerOne == 'X':
        print('Você começa!!!')
        while True:
            play = input('Sua vez!!! Escolha onde irá jogar: ')
            funv.play(inicial, play, playerOne)
            funv.printlista(inicial)
            resultado = funv.checkwin(inicial, playerOne, playerTwo)
            if resultado != 'continua':
                break
            funv.playpc(inicial, playerTwo)
            funv.printlista(inicial)
            resultado = funv.checkwin(inicial, playerOne, playerTwo)
            if resultado != 'continua':
                break
    else:
        print('O computador começa!!!')
        while True:
            # Lance do computador
            print('O computador faz um lance: ')
            funv.playpc(inicial, playerTwo)
            funv.printlista(inicial)
            resultado = funv.checkwin(inicial, playerOne, playerTwo)
            if resultado != 'continua':
                break
            # Lance do jogador
            play = input('Sua vez!!! escolha onde irá jogar: ')
            funv.play(inicial, play, playerOne)
            funv.printlista(inicial)
            resultado = funv.checkwin(inicial, playerOne, playerTwo)
            if resultado != 'continua':
                break


# Modo de jogo local
else:
    print('\nO JOGO IRÁ COMEÇAR')
    funv.printlista(inicial)
    print(f'O player {playerOne} começa!!!')
    while True:
        # Jogador 1
        play = input(f'Vez do jogador {playerOne}: ')
        funv.play(inicial, play, playerOne)
        funv.printlista(inicial)
        resultado = funv.checkwin(inicial, playerOne, playerTwo)
        if resultado != 'continua':
            break

        # Jogador 2
        play = input(f'Vez do jogador {playerTwo}: ')
        funv.play(inicial, play, playerTwo)
        funv.printlista(inicial)
        resultado = funv.checkwin(inicial, playerOne, playerTwo)
        if resultado != 'continua':
            break


# Mostra o resultado dos jogos
if resultado[0] == 'win':
    print(f'O jogador {playerOne} venceu na {resultado[1]}!')
elif resultado[0] == 'lost':
    print(f'O jogador {playerTwo} venceu na {resultado[1]}!')
elif resultado == 'O jogo deu Velha':
    print(f'{resultado}, tente novamente. :(')
