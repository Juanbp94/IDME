""""Un programa que lea por teclado una frase y nos devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena."""


from os import system



letras= {}
letra = ""
frase = ""


system("cls")


frase = input("Teclea la frase ")

for letra in frase:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

print(letras)