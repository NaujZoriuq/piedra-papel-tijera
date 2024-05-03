import random

opciones = ('piedra', 'papel', 'tijera')

computador_gano = 0
usuario_gano = 0

ronda = 1

while True:

    print('*' *15)
    print('<--- RONDA --->' ,ronda)
    print('*' *15)
    print('')
    print('Ganó computadora --->', computador_gano)
    print('Ganó usuario --->', usuario_gano)
    print('*' *15)
    print('')


    seleccion_usuario = input("Piedra, Papel o Tijera -->  ")
    seleccion_usuario = seleccion_usuario.lower()

    ronda +=1

    if not seleccion_usuario in opciones:
        print("Opción no valida")
        continue


    seleccion_computador = random.choice(opciones)

    print('*' *15)
    print('Selección de usuario --> ', seleccion_usuario)
    print('Selección de computador --> ', seleccion_computador)
    print('')

    if seleccion_usuario == seleccion_computador:
        print("Empate!")
    elif seleccion_usuario == 'piedra':
        if seleccion_computador == 'tijera':
            print("Piedra gana a Tijera")
            print("Usuario ganó")
            usuario_gano += 1
        else:
            print("Papel gana a Piedra")
            print("Computador ganó!")
            computador_gano += 1
    elif seleccion_usuario == 'papel':
        if seleccion_computador == 'piedra':
            print("Papel gana a Piedra")
            print("Usuario ganó!")
            usuario_gano += 1
        else:
            print("Tijera gana a Papel")
            print("Computador ganó!")
            computador_gano += 1
    elif seleccion_usuario == 'tijera':
        if seleccion_computador == 'papel':
            print("Tijera gana a Papel")
            print("Usuario ganó!")
            usuario_gano += 1
        else:
            print("Piedra gana a Tijera")
            print("Computador ganó!")
            computador_gano += 1

        print('')
        print('*' *15)
        if computador_gano == 3:
            print('El ganador final ha sido el compuador con: ', computador_gano)
            break

        if usuario_gano == 3:
            print('El ganador final ha sido el usuario con: ', usuario_gano)
            break