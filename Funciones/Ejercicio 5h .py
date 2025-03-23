"""Funcion que devuelva el valor de una resistencia de 4 bandas, indicando su intervalo. Habra que pasarle los colores de las 4 bandas
El formato sera; resistencia(color1,color2,color3,color4)--> (valor norminal, limite inferio y limite superior)"""

from os import system


color1,color2,color3,color4 = 0, 0, 0, 0

resultado=[]

def resistencia(color1,color2,color3,color4):

    coloresValores= {"Negro":0, "Marron":1, "Rojo":2, "Naranja":3, "Amarillo":4, "Verde":5, "Azul":6, "Violeta":7, "Gris":8, "Blanco":9}
    tolerancias = {"Rojo":2, "Dorado":5, "Plata":10}

    valorNominal = coloresValores[color1]*10 + coloresValores[color2] * 10**coloresValores[color3] 
    limiteInferior = valorNominal - valorNominal * tolerancias[color4] /100
    limiteSuperior = valorNominal + valorNominal * tolerancias[color4] /100

    return(valorNominal,limiteInferior, limiteSuperior)



system("cls")



color1 = input("Teclea el primer color: ")
color2 = input("Teclea el segundo color: ")
color3 = input("Teclea el tercero color: ")
color4= input("Teclea el cuarto color: ")

color1=color1.capitalize()
color2=color2.capitalize()
color3 = color3.capitalize()
color4 = color4.capitalize()
resultado = resistencia(color1,color2,color3,color4)

print(f"El valor nominal de la resistencia es: {resultado[0]} ")
print(f"El intervalo es ({resultado[1]}, {resultado[2]})")
