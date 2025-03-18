"""  Programa que escriba una funcion que reciba como parametro una cadena de poalabras separadas por 
espacios y devuelva , como resutlado, cuantas palabras de mas de cinco letras tiene la cadena dada"""


from os import system


frase = ""





def contarPalabras(frase):


    j=0
    letra=0
    contadorPalabras = 0

    for letra in range(0,len(frase)):
        if letra ==" ":
            if j >4:
                contadorPalabras +=1
            j = 1
        j += 1
    if j > 4:
            contadorPalabras +=1
    return contadorPalabras


system("cls")

frase = input("introduce la frase a escanear: ")
print(contarPalabras(frase))


