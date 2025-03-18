

from os import system


palabra = ""

i = 1 
numVeces = 0




system("cls")

palabra = input("Introduce la palabra a comprobar si es un palindromo o no: ")

palabra = palabra.lower()   

if len(palabra)%2 ==1:
    numVeces = len(palabra)/2 - 1
else:
    numVeces = len(palabra) /2     

while i <= numVeces and palabra[i-1] == palabra[-1]:
    i= i+1
if i > numVeces and palabra[i-1] == palabra[-1]:
    print(f"La palabra {palabra} si es un palindromo. ")
else:
    print(f"La palabra {palabra} no es un palindromo. ")


