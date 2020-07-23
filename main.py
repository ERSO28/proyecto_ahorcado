from funciones import limpiador_consola
from diccionario import lista_palabras
from diccionario import lista_significados
import random


def obtener_palabra():
    palabra = lista_palabras[indice]
    return palabra


def obtener_signficado():
    significado = lista_significados[indice]
    return significado


switch = True
print('AHORCADO')
while switch:
    indice = random.randint(0, 9)
    palabra_secreta = obtener_palabra()
    significado_palabra = obtener_signficado()
    print(significado_palabra)
    palabra_oculta = '-' * len(palabra_secreta)
    errores = 0
    letras_usuario = set()
    while errores < 6:
        print(palabra_oculta)
        print(palabra_secreta)
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
        limpiador_consola.limpiador()
        switch = True
    elif usuario_pass == 'n':
        limpiador_consola.limpiador()
        switch = False
        print('Gracias por haber jugado.')
        break
    else:
        usuario_pass = input('Introduzca un caracter valido.')

    # TODO: Agregar funcion para diseño de muñecos.
