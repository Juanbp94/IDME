#Resuelve una ecuación de 2º grado, ax2+bx+c = 0, introduciendo los coeficientes a, b y c.
#Importacion de librerias
from math import sqrt

#las variables de la formula
a=0
b=0
c=0
x1 = 0
x2 = 0 

print("Ecuación de segundo grado: ax^2 + bx + c = 0")

a = float(input("Introduce la variable de grado 2 llamada a"))
b = float(input("Introduce la variable de grado 1 llamada b"))
c = float(input("Introduce la variable de grado 0 llamada c"))

print(f"Nuestra Ecuación de segundo grado: {a}x^2 + {b}x + {c} = 0")

# los parentesis de la -b no son necesarios
x1 = (-(b) + sqrt(b**2+4*a*c))/(2*a)
x2 = (-(b) - sqrt(b**2+4*a*c))/(2*a)

print(f"Las soluciones a esa ecuacion seria : {x1} y {x2}")

