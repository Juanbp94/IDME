from os import system 

matriz = [[0,0],[0,0]]
determinante = 0
fila = 0
columna = 0



system("cls")

for fila in range (0,2):
    for columna in range (0,2):

        matriz[fila,columna] = float(input(f"Teclea la posicion fila {fila}, columna {columna} de la matriz: "))


determinante = matriz[0,0] * matriz[1,1] - matriz[0,1]*matriz[1,0]

print(f"La solucion del determinante de la matriz es: {determinante} ")