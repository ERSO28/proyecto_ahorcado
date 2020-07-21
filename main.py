import random
import os


def limpiador():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')


palabra_secreta = random.choice(['cesped', 'sol', 'pasto', 'python'])
palabra_oculta = '-' * len(palabra_secreta)
errores = 0
bandera = True
letras_usuario = set()

print('AHORCADO')
while errores < 8:
    print(palabra_oculta)
    # print(palabra_secreta)
    if palabra_oculta in palabra_secreta:
        print('Lo lograste!')
        break
    else:
        letra = input('Ingresa una letra: ')
        limpiador()
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

# TODO: Implementar "While" para volver a inciar programa.
# TODO: Agregar diccionario de palabras.
# TODO: Agregar funcion para diseño de muñecos.
