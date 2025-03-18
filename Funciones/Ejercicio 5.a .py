"""Una funcion que devuelva  True si un valor parametro esta dentro de un rangom que tambien introduciremos como  parametros. Si no es asi, devolvera False."""


from os import system

numero = 0

limiteInferior=0
limiteSuperior = 0

def intervalo(num, limInferior, limSuperior):
    if num >= limInferior and num <= limSuperior:
        return True
    else:
        return False

system("cls")

print(intervalo(4,23,65))

