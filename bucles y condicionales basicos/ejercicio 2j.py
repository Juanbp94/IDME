#Pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto.

#variables

numero= 1
suma = 0
multiplicacion=1

from os import system

system("cls")

#programa


while numero!=0:
    numero = float(input("Introduce un numero siendo el 0 para terminar el programa "))
    suma = numero + suma
    if numero !=0:
        multipllicacion= multiplicacion*numero

print(f"La suma total de los numeros es {suma} mientras que la multiplicacion total es {multiplicacion} .")
