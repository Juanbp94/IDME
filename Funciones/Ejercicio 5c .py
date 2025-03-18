"""Al introducir un valor numerico natural por teclado que nos diga si es un numero primo o no"""

from os import  system

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i ==0:
            return False
    return True


system("cls")

numero = int(input("Introduce un valor para comprobar si es numero primo: "))
if esPrimo(numero) == True:
    print("El numero introducido es primo ")
else:
    print("El numero introducido No es primo ")