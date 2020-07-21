from funciones import limpiador_consola
import random


switch = True
print('AHORCADO')
while switch:
    palabra_secreta = random.choice(['cesped', 'sol', 'pasto', 'python'])
    palabra_oculta = '-' * len(palabra_secreta)
    errores = 0
    letras_usuario = set()
    while errores < 8:
        print(palabra_oculta)
        # print(palabra_secreta)
        if palabra_oculta in palabra_secreta:
            print('Lo lograste!')
            break
        else:
            letra = input('Ingresa una letra: ')
            limpiador_consola.limpiador()
            if len(letra) != 1:
                print('Debes ingresar una sola letra.')
            elif not (letra.isalpha()):
                print('Introduce una letra del alfabeto.')
            else:
                if letra in letras_usuario:
                    print('Ya ingresaste esta letra.')
                elif letra not in palabra_secreta:
                    errores += 1
                else:
                    for i in range(len(palabra_secreta)):
                        if letra == palabra_secreta[i]:
                            palabra_listada = list(palabra_oculta)
                            palabra_listada[i] = letra
                            palabra_oculta = ''.join(palabra_listada)
            letras_usuario.add(letra)
    else:
        print('Se acabaron los intentos')
    usuario_pass = input('Desea seguir jugando?. (s/n)').lower()
    if usuario_pass == 's':
        switch = True
    elif usuario_pass == 'n':
        switch = False
        print('Gracias por haber jugado.')
        break
    else:
        usuario_pass = input('Introduzca un caracter valido.')

    # TODO: Agregar diccionario de palabras.
    # TODO: Agregar funcion para diseño de muñecos.
