#Que sume los primeros N números pares.

#variables

numerosPares = 0
numeroVariable = 0
contador= 0
suma= 0

numeroVariable = int(input("Introduce la cantidad de numeros pares que quieres que se sumen "))

"""

for numerosPares in range(0,2*numeroVariable,2):
    contador +=1
    suma = numerosPares + suma


print(f"La suma total de los primeros {numeroVariable} es: {suma} ")


"""




while numerosPares <=numeroVariable*2:
    contador +=1
    numerosPares +=2
    suma = suma + numerosPares

print(f"La suma total de los primeros {numeroVariable} es: {suma}")

