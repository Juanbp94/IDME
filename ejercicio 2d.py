#Que introduzca por teclado el valor de la nota de un examen y diga si está aprobado o suspenso (>=5).

#Variables

nota = 0

#Programa principal

nota = float(input("Introduce la nota del alumno "))


if nota>= 5:
    print("Este alumno esta aprobado")

else:
      print("Este alumno esta suspenso")