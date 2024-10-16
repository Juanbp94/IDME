#(Estructura “elif”) Pide por teclado un valor entre 1 y 7 y debe indicarnos por pantalla el día de la semana correspondiente.

#variables

valor=0 
from os import system

#Programa


system("cls")

valor = int(input("Introduce un valor de 1 al 7 para indicar el dia de la semana siendo 1 el lunes y 7 el domingo "))

if valor ==1 :
    print("El dia comunicado es lunes")
elif valor ==2:
        print("El dia comunicado es martes")
elif valor ==3:
          print("El dia comunicado es miercóles")
elif valor == 4:
           print("El dia comunicado es jueves")
elif valor ==5:
            print("El dia comunicado es viernes")
elif valor ==6:
            print("El dia comunicado es sabado")
elif valor ==7:
            print("El dia comunicado es domingo")




