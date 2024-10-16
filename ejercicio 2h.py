#Que el usuario introduzca un número por teclado y se asegure que está entre 1 y 10 (ambos incluídos). Si no lo es, que vuelva a pedirlo hasta que lo sea. Al final, muéstralo en pantalla.

from os import system

system("cls")

# variables

numero= 0

# programa

while numero < 1 or numero > 10:
    numero = float(input("Introduce un numero entre 1 y 10 "))

print(f"El numero introducido es {numero}")

