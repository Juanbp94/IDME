"""Escribir un programa que cree un diccionario simulando una cesta de la compra.
 El programa debe preguntar el artículo y su precio y añadirlo al diccionario, hasta que el usuario decida terminar. 
 Después se debe mostrar por pantalla la lista de la compra y el coste total."""


 from os import system

 
 compra = {}
 producto = " "
 precio = 0
 importeTotal = 0

 system("cls")

 while producto != "":
    producto = input("Teclea el producto ")
    if producto != "":
        precio = float(input("Introduce el precio del producto. "))
        compra[producto] = precio
    print("")

for producto in compra:
    print(f"Articulo: {producto}, precio : {compra[producto]}")
    importeTotal = importeTotal + compra[precio]

print(f"El precio total de la compra es: {importeTotal}")




