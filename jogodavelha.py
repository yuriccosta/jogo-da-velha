import funcoes as fv

# Feito por zzAlfa / Versão 1.0

inicial = ['( )', '( )', '( )',
           '( )', '( )', '( )',
           '( )', '( )', '( )'
           ]
print('Bem vindo ao Jogo da Velha')
fv.listaatual(inicial)
while True:
    choice = input('Qual você escolhe? X ou O ').upper()
    if choice == 'X':
        print(f'Você escolheu {choice}')
        sec = 'O'
        break
    elif choice == 'O':
        print(f"Você escolheu {choice}")
        sec = 'X'
        break
    else:
        print('Tente novamente, sua escolha não foi válida.')
        print('Tente digitar "X" ou "O"')
        print('')
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
if modo == 'solo':
    print('')
    print('O JOGO IRÁ COMEÇAR')
    fv.listaatual(inicial)
    if choice == 'X':
        play = int(input('Você começa!!! Escolha onde irá jogar: '))
        fv.play(inicial, play, choice)
        fv.playpc(inicial, sec)
        fv.listaatual(inicial)
        while True:
            play = int(input('Sua vez!!! Escolha onde jogar novamente: '))
            fv.play(inicial, play, choice)
            fv.listaatual(inicial)
            resultado = fv.checkwin(inicial, choice, sec)
            if resultado[0] == 'win':
                print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
                break
            elif resultado[0] == 'lost':
                print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
                break
            elif resultado == 'O jogo deu Velha':
                print(f'{resultado}, tente novamente.')
                break
            fv.playpc(inicial, sec)
            fv.listaatual(inicial)
            resultado = fv.checkwin(inicial, choice, sec)
            if resultado[0] == 'win':
                print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
                break
            elif resultado[0] == 'lost':
                print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
                break
            elif resultado == 'O jogo deu Velha':
                print(f'{resultado}, tente novamente.')
                break

    else:
        print('O computador faz o primeiro lance')
        fv.playpc(inicial, sec)
        fv.listaatual(inicial)
        play = int(input('Sua vez!!! escolha onde irá jogar: '))
        fv.play(inicial, play, choice)
        fv.listaatual(inicial)
        while True:
            print('O computador faz um lance: ')
            fv.playpc(inicial, sec)
            fv.listaatual(inicial)
            resultado = fv.checkwin(inicial, choice, sec)
            if resultado[0] == 'win':
                print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
                break
            elif resultado[0] == 'lost':
                print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
                break
            elif resultado == 'O jogo deu Velha':
                print(f'{resultado}, tente novamente.')
                break
            play = int(input('Sua vez!!! Escolha onde jogar novamente: '))
            fv.play(inicial, play, choice)
            fv.listaatual(inicial)
            resultado = fv.checkwin(inicial, choice, sec)
            if resultado[0] == 'win':
                print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
                break
            elif resultado[0] == 'lost':
                print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
                break
            elif resultado == 'O jogo deu Velha':
                print(f'{resultado}, tente novamente.')
                break


elif modo == 'local':
    print('')
    print('O JOGO IRÁ COMEÇAR')
    fv.listaatual(inicial)
    play = int(input(f'O player {choice} começa!!! Escolha onde irá jogar: '))
    fv.play(inicial, play, choice)
    fv.listaatual(inicial)
    play = int(input(f'Vez do jogador {sec}!!! Escolha onde irá jogar: '))
    fv.play(inicial, play, sec)
    fv.listaatual(inicial)
    while True:
        play = int(input(f'Vez do jogador {choice}!!! Escolha onde jogar novamente: '))
        fv.play(inicial, play, choice)
        fv.listaatual(inicial)
        resultado = fv.checkwin(inicial, choice, sec)
        if resultado[0] == 'win':
            print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
            break
        elif resultado[0] == 'lost':
            print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
            break
        elif resultado == 'O jogo deu Velha':
            print(f'{resultado}, tente novamente.')
            break
        play = int(input(f'Vez do jogador {sec}!!! Escolha onde jogar novamente: '))
        fv.play(inicial, play, sec)
        fv.listaatual(inicial)
        resultado = fv.checkwin(inicial, choice, sec)
        if resultado[0] == 'win':
            print(f'Você venceu!!! O jogador {choice} venceu na {resultado[1]}')
            break
        elif resultado[0] == 'lost':
            print(f'Você perdeu!!! O jogador {sec} venceu na {resultado[1]}')
            break
        elif resultado == 'O jogo deu Velha':
            print(f'{resultado}, tente novamente.')
            break
