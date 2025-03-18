"""Realiza un programa que pida por teclado una serie de asignaturas, con su calificación correspondiente, hasta que introduzca una asignatura en blanco. 
Posteriormente nos debe mostrar por pantalla la lista de las que están aprobadas (calificación mayor o igual que 5), 
con su correspondiente nota y la media aritmética de todas las calificaciones (se incluirán también las notas suspensas en la media). """



from os import system

asignaturas = {}

nombreAsignatura = " "
nota = 0
sumaCalificaciones= 0


system("cls")


while nombreAsignatura !="":
    nombreAsignatura = input("Teclea el nombre de la asignatura: ")
    if nombreAsignatura!="":
        nota = float(input("Introduce la calificacion de la asignatura: "))
        asignaturas [nombreAsignatura] = nota
    print(" ")


for nombreAsignatura in asignaturas:
    if asignaturas[nombreAsignatura] >=5:
        print(f"La asignatura {nombreAsignatura} esta aprobada con un {asignaturas[nombreAsignatura]} ")
    sumaCalificaciones = sumaCalificaciones + asignaturas[nombreAsignatura]

print(" ")

print(f"La media aritmetica de las calificaciones es: {sumaCalificaciones/lend(asignaturas)} ")




