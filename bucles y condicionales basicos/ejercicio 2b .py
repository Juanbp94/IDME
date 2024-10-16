#Que sume los primeros 50 números impares.

#Variables

numeroImpar = 0
contador= 0
suma= 0

# Programa

for numeroImpar in range(1,101,2):
    contador +=1
    #print(numeroImpar) no es necesario solo si quiero que se muestren los numeros impares
    suma= suma + numeroImpar

print(f"cantidad de numeros contados es :{contador}")
print(f"La suma total de los 50 primeros numeros primos es: {suma}")