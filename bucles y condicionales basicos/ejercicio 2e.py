#Que lea por teclado 2 números y diga cuál es mayor (supondremos que son diferentes)
from os import system
#variables

numero1 = 0
numero2 = 0

#Comando que ejecuta comando de windows hay que immportar la libreria os (SO)  con un asterisco se importa toda la libreria *

system("cls")

#Programa
numero1 = int(input("Teclea el primer numero"))

numero2 = int(input("Teclea el segundo numero"))


if numero1>numero2:
    print("El primer numero es mayor que el segundo ")
else:
    print("El segundo numero es mayor que el primero")




