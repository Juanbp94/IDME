



from os import system 

matriz = [[0,0],[0,0]]
determinante = 0



system("cls")


matriz[0,0] = float(input("Teclea la posicion superior izquierda de la matriz: "))
matriz[0,1] = float(input("Teclea la posicion superior derecha de la matriz: "))
matriz[1,0] = float(input("Teclea la posicion abajo izquierda de la matriz: "))
matriz[0,1] = float(input("Teclea la posicion abajo derecha de la matriz: "))


determinante = matriz[0,0] * matriz[1,1] - matriz[0,1]*matriz[1,0]

print(f"La solucion del determinante de la matriz es: {determinante} ")