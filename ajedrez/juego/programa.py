

import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Ajedrez')
font = pygame.font.SysFont('Arial', 30)
bigFont = pygame.font.SysFont('arial',50)
timer = pygame.time.Clock()
fps = 60

#piezas

white =['torre','caballo', 'alfil','rey', 'reina','alfil','caballo','torre',
           'peon','peon','peon','peon','peon','peon','peon','peon',]

whitePlaces = [(0,0),(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                (0,1),(1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black =['torre','caballo', 'alfil','rey', 'reina','alfil','caballo','torre',
           'peon','peon','peon','peon','peon','peon','peon','peon',]
blackPlaces = [(0,7),(1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                (0,6),(1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

comidasBlancas = []
comidasNegras = []
#0 - turno de blancas, sin seleccion --> 1 turno de blancas, con seleccion --> 2 turno de negras , sin seleccion --> 3 turno de negras con seleccion
pasoTurno = 0
seleccion = 100
movimientosValidos = []

#imagenes de las piezas y escalado para el tablero (revisar tamaños segun pantalla)

reinaBlanca = pygame.image.load('imagenes/reinab.png')
reinaBlanca = pygame.transform.scale(reinaBlanca, (80,80))
reinaBlancaPeque = pygame.transform.scale(reinaBlanca, (45,45))
reyBlanco = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/reyb.png')
reyBlanco = pygame.transform.scale(reyBlanco, (80, 80))
reyBlancoPeque = pygame.transform.scale(reyBlanco, (45, 45))
torreBlanca = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/torreb.png')
torreBlanca = pygame.transform.scale(torreBlanca, (80, 80))
torreBlancaPeque = pygame.transform.scale(torreBlanca, (45, 45))
alfilBlanco = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/alfilb.png')
alfilBlanco = pygame.transform.scale(alfilBlanco, (80, 80))
alfilBlancoPeque = pygame.transform.scale(alfilBlanco, (45, 45))
caballoBlanco = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/caballob.png')
caballoBlanco = pygame.transform.scale(caballoBlanco, (80, 80))
caballoBlancoPeque = pygame.transform.scale(caballoBlanco, (45, 45))
peonBlanco = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/peonb.png')
peonBlanco = pygame.transform.scale(peonBlanco, (65, 65))
peonBlancoPeque = pygame.transform.scale(peonBlanco, (45, 45))
imagenesBlancas = [peonBlanco,reinaBlanca, reyBlanco, torreBlanca, alfilBlanco, caballoBlanco]
magenesBlancasPeque = [peonBlancoPeque,reinaBlancaPeque, reyBlancoPeque, torreBlancaPeque, alfilBlancoPeque, caballoBlancoPeque]

reinaNegra = pygame.image.load('imagenes/reinan.png')
reinaNegra = pygame.transform.scale(reinaNegra, (80, 80))
reinaNegraPeque = pygame.transform.scale(reinaNegra, (45, 45))
reyNegro = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/reyn.png')
reyNegro = pygame.transform.scale(reyNegro, (80, 80))
reyNegroPeque = pygame.transform.scale(reyNegro, (45, 45))
torreNegra = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/torren.png')
torreNegra = pygame.transform.scale(torreNegra, (80, 80))
torreNegraPeque = pygame.transform.scale(torreNegra, (45, 45))
alfilNegro = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/alfiln.png')
alfilNegro = pygame.transform.scale(alfilNegro, (80, 80))
alfilNegroPeque = pygame.transform.scale(alfilNegro, (45, 45))
caballoNegro = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/caballon.png')
caballoNegro = pygame.transform.scale(caballoNegro, (80, 80))
caballoNegroPeque = pygame.transform.scale(caballoNegro, (45, 45))
peonNegro = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/peonn.png')
peonNegro = pygame.transform.scale(peonNegro, (65, 65))
peonNegroPeque = pygame.transform.scale(peonNegro, (45, 45))
imagenesNegras = [peonNegro,reinaNegra, reyNegro, torreNegra, alfilNegro, caballoNegro]
magenesNegrasPeque = [peonNegroPeque,reinaNegraPeque, reyNegroPeque, torreNegraPeque, alfilNegroPeque, caballoNegroPeque]

ListaPiezas = ['peon', 'reina', 'rey', 'torre','alfil','caballo' ]

#dibujo del tablero

def tablero():
    for i in range(32):
        column = i % 4
        row = i//4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'blue', [600 - (column * 200), row * 100, 100,100],)
        else:
             pygame.draw.rect(screen, 'blue', [700 - (column * 200), row * 100, 100,100],)
        pygame.draw.rect(screen, 'aquamarine4', [0,800, WIDTH , 100])
        pygame.draw.rect(screen, 'red', [0,800, WIDTH , 100], 5)
        pygame.draw.rect(screen, 'yellow', [800,0, 200 , HEIGHT], 10)
        infoTurno = ['Blancas elige pieza a mover', 'Blancas elige destino', 'Negras elige pieza a mover', 'Negras elige destino', ]
        screen.blit(bigFont.render(infoTurno[pasoTurno], True, 'black'),(20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0,100*i), (800,100*i), 2)
            pygame.draw.line(screen, 'black', (100*i,0), (100*i,800), 2)

#movimientos de piezas en el tablero

def Piezas():
    for i in range(len(white)):
        index = ListaPiezas.index(white[i])
        if white[i] == 'peon' :
            screen.blit(peonBlanco, (whitePlaces[i][0] * 100 + 22, whitePlaces [i][1]* 100 +30))
        else:
            screen.blit(imagenesBlancas[index], (whitePlaces[i][0] * 100 + 10, whitePlaces [i] [1]* 100 +10))
        if pasoTurno < 2 and seleccion < len(whitePlaces):
            if seleccion ==i:
                pygame.draw.rect(screen, 'red',[whitePlaces[i][0] *100 +1, whitePlaces[i][1]*100 + 1, 100,100], 2)


    for i in range(len(black)):
        index = ListaPiezas.index(black[i])
        if black[i] == 'peon' :
            screen.blit(peonNegro, (blackPlaces[i][0] * 100 + 22, blackPlaces [i] [1]* 100 +30))
        else:
            screen.blit(imagenesNegras[index], (blackPlaces[i][0] * 100 + 10, blackPlaces [i] [1]* 100 +10))
        if pasoTurno >= 2 and seleccion < len(blackPlaces):
            if seleccion ==i:
                pygame.draw.rect(screen, 'red',[blackPlaces[i][0] *100 +1, blackPlaces[i][1]*100 + 1, 100,100], 2)

# movimiento del peon

def revisaPeon(posicion, color):
   listaMovimientos=[]
   if color == 'blanco':
        if (posicion[0],posicion[1]+1) not in whitePlaces and (posicion[0], posicion[1]+1) not in blackPlaces and posicion[1]<7:
            listaMovimientos.append((posicion[0], posicion[1]+1)) # si el peon esta sin tocar se mueve 1
        if (posicion[0],posicion[1]+2) not in whitePlaces and (posicion[0], posicion[1]+2) not in blackPlaces and posicion[1]==1:
            listaMovimientos.append((posicion[0], posicion[1]+2))  # si el peon esta sin tocar se mueve 2  
        if (posicion[0] +1, posicion[1]+1) in blackPlaces:
            listaMovimientos.append(posicion[0]+1, posicion[1]+1)
        if (posicion[0]-1, posicion[1]+1) in blackPlaces:
            listaMovimientos.append((posicion[0]-1, posicion[1]+1))
   else:
        if (posicion[0],posicion[1]-1) not in whitePlaces and (posicion[0], posicion[1]-1) not in blackPlaces and posicion[1]>0:
            listaMovimientos.append((posicion[0], posicion[1]-1)) 
        if (posicion[0],posicion[1]+2) not in whitePlaces and (posicion[0], posicion[1]-2) not in blackPlaces and posicion[1]==6:
            listaMovimientos.append((posicion[0], posicion[1]-2))  
        if (posicion[0] +1, posicion[1]-1) in blackPlaces:
            listaMovimientos.append(posicion[0]+1, posicion[1]-1)
        if (posicion[0]-1, posicion[1]-1) in blackPlaces:
            listaMovimientos.append((posicion[0]-1, posicion[1]-1))


   """
def revisa_peon(posicion, color):
    listaMovimientos = []
    x, y = posicion

    if color == 'blanco':
        # Movimiento normal hacia adelante (si la casilla está libre)
        if (x, y + 1) not in whitePlaces and (x, y + 1) not in blackPlaces:
            listaMovimientos.append((x, y + 1))
        
        # Primer movimiento doble
        if y == 1 and (x, y + 2) not in whitePlaces and (x, y + 2) not in blackPlaces:
            listaMovimientos.append((x, y + 2))
        
        # Captura en diagonal
        if (x + 1, y + 1) in blackPlaces:
            listaMovimientos.append((x + 1, y + 1))
        if (x - 1, y + 1) in blackPlaces:
            listaMovimientos.append((x - 1, y + 1))

    else:  # Peón negro
        if (x, y - 1) not in whitePlaces and (x, y - 1) not in blackPlaces:
            listaMovimientos.append((x, y - 1))
        
        if y == 6 and (x, y - 2) not in whitePlaces and (x, y - 2) not in blackPlaces:
            listaMovimientos.append((x, y - 2))
        
        # Captura en diagonal
        if (x + 1, y - 1) in whitePlaces:
            listaMovimientos.append((x + 1, y - 1))
        if (x - 1, y - 1) in whitePlaces:
            listaMovimientos.append((x - 1, y - 1))

    return listaMovimientos
"""





def revisaMovimientosValidos():
    if pasoTurno <2:
        listaOpciones = opcionesBlancas
    else:
        listaOpciones = opcionesNegras
    opcionesValidas=listaOpciones[seleccion]
    return opcionesValidas


#movimientos validos en tablero

def valido(movimientos):
    if pasoTurno < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(movimientos)):
        pygame.draw.circle(screen, color, (movimientos[i][0] * 100 + 50, movimientos[i][1] * 100 + 50), 5)


#opciones validas en el tablero

def opcionesPosibles(piezas, lugares, turno):
    listaMovimientos = []
    listaTodosMovimientos =[]
    for i in range((len(piezas))):
        posicion = lugares[i]
        pieza = piezas[i]
        if pieza == 'peon':
            listaMovimientos = revisaPeon(posicion, turno)
        #elif pieza == 'torre':
         #   listaMovimientos = revisaTorre(places, turno)
        #elif pieza == 'alfil':
       #     listaMovimientos = revisaAlfil(places, turno)
        #elif pieza == 'caballo':
        #    listaMovimientos = revisaCaballo(places, turno)
        #elif pieza == 'rey':
        #    listaMovimientos = revisaRey(places, turno)
        #elif pieza == 'reina':
        #    listaMovimientos = revisaReina(places, turno)

        listaTodosMovimientos.append(listaMovimientos)


    return listaTodosMovimientos 

#juego principal

opcionesNegras= opcionesPosibles(black, blackPlaces,'negro')
opcionesBlancas= opcionesPosibles(white, whitePlaces,'blanco')
run = True
while run:
    timer.tick(fps)
    screen.fill('pink')  # Limpia la pantalla en cada frame

    tablero()  # Dibuja el tablero
    Piezas()  # Dibuja las piezas

    if seleccion != 100:
        movimientosValidos = revisaMovimientosValidos()
        valido(movimientosValidos)
     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)

            if pasoTurno <= 1:
                if click_coords in whitePlaces:
                    seleccion = whitePlaces.index(click_coords)
                    if pasoTurno == 0:
                        pasoTurno = 1
                elif click_coords in movimientosValidos and seleccion != 100:
                    whitePlaces[seleccion] = click_coords  # Actualiza la posición
                    pasoTurno = 2  # Cambia de turno
                    seleccion = 100
                    movimientosValidos = []

            if pasoTurno > 1:
                if click_coords in blackPlaces:
                    seleccion = blackPlaces.index(click_coords)
                    if pasoTurno == 2:
                        pasoTurno = 3
                elif click_coords in movimientosValidos and seleccion != 100:
                    blackPlaces[seleccion] = click_coords
                    pasoTurno = 0
                    seleccion = 100
                    movimientosValidos = []

    pygame.display.update() #¡ACTUALIZA LA PANTALLA!


    
pygame.quit()
