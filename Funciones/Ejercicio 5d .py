"""Reutilizando la funcion usada  en el apartado anterior, debemos indicar si son primos o no los valores numericos de un rango introducido por teclado"""

from os import system


numero = 0
limiteInferior= 0
limiteSuperior=0

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i ==0:
            return False
    return True


system("cls")


limiteInferior = int(input("Introduce el valor inferior del intervalo a comprobar "))
limiteSuperior = int(input("Introduce el valor inferior del intervalo a comprobar "))

for numero in range(limiteInferior, limiteSuperior + 1):
    if esPrimo(numero) ==True:
        print(f"El numero {numero} Si es primo. ")
    else:
        print(f"El numero {numero} No es primo. ")
