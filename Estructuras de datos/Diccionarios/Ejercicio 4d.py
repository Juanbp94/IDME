

"""   El usuario tendrá un máximo de 3 intentos, y al acceder correctamente se mostrará un mensaje de bienvenida, con el nombre y apellidos del usuario.""" 




from os import system


usuarios = {
	"aexposito":
	    {"nombre": "Antonio",
		    "apellidos": {"primerApellido": "Expósito", "segundoApellido": "Núñez"},
	    "password": "123456"},
	"fgonzalez":
	    {"nombre": "Francisco",
		    "apellidos": {"primerApellido": "González", "segundoApellido": "Martínez"},
	    "password": "jejejaja"},
	"lcastillo":
	    {"nombre": "Lourdes",
		    "apellidos": {"primerApellido": "Prieto", "segundoApellido": "Valverde"},
	    "password": "6789"}
	    }


usuario= ""
contraseña = ""
numIntentos = 0
valido = False



system("cls")



while numIntentos <3 and valido == False:
	usuario = input("Introduce el usuario: ")
	contraseña = input("Contraseña: ")
	numIntentos += 1
	if usuario in usuarios and contraseña == usuarios[usuario]["password"]:
		valido = True
		print(f"Bienvenido {usuarios[usuario]["nombre"]} {usuarios[usuario]["apellidos"]["primerApellido"]} {usuarios[usuario]["apellidos"]["segundoApellido"]}")
	else:
		print(f"La combinancion de usuario y contraseña no es valido. Te quedan {3-numIntentos} ")
		valido = False
		input("Pulsa enter para continuar. ")


