# Que muestre en pantalla los primeros 50 números pares.

#variables
contador = 0
numero = 0

for numero in range(0,100,2):
    print(numero)
    contador = contador +1 # tambien se puede poner como +=1
    
print(f"El numero de valores contados es {contador}")