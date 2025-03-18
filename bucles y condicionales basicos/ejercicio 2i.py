#Que sume todos los números pares positivos, partiendo desde 0, hasta que la suma supere el valor de 1000. Posteriormente, debe mostrar en pantalla cuál es el valor de la suma y cuántos números se han sumado.

#variables

suma = 0
numero = 0
contador = 0

#importacion de libreriras

from os import system


system("cls")



#programa

while suma<= 1000:
    suma = suma +numero
    numero +=2
    contador +=1

print (f"la suma de los primeros  {contador} numeros pares da  {suma}")