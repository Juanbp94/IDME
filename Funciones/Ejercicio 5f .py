"""Programa una fruncion que aplique un descuento a un precio dado. Tomara dos parametros, el precio y el porcentaje de descuento. Devolvera el importe del precio con el descuento 
aplicado 
Valida que el descuento esten entre 0 y 100. En caso contrario , imprimer mensaje de error devuelve -1.
Añade un parametro opcional, llamado "impuestos", que sera el procentaje de impuestos a aplaicar. En caso de no utilizar el parametro, se atendera que no hay impuestos a a aplicar"""
2


from os import system



precio = 0
porcentajeDescuento = 0
porcentajeImpuestos = 0



def calculoImporte(precio,descuento, impuesto=0):
    if descuento < 0 or descuento >100:
        print("Error: el descuento debe de  estar entre 0 y 100 %. ")
        return -1
    return precio * (1-descuento/100) * (1+ impuesto/100)


system("cls")

precio = float(input("Introduce el precio del articulo. "))
porcentajeDescuento = float(input("Introduce el descuento del articulo. "))
porcentajeImpuestos = input("Introduce el procentaje del impuesto. ")

if porcentajeImpuestos == "":
    print(f"El importe final es: {calculoImporte(precio,porcentajeDescuento)}")
else:
    print(f"El importe final es: {calculoImporte(precio, porcentajeDescuento,float(porcentajeImpuestos))}")