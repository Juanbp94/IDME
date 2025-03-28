

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
seleccion = 500
movimientosValidos = []

#imagenes de las piezas y escalado para el tablero (revisar tamaños segun pantalla)

reinaBlanca = pygame.image.load('ajedrez/juego/imagenes/reinab.png')
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

reinaNegra = pygame.image.load('ajedrez/juego/imagenes/reinan.png')
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


    for i in range(len(black)):
        index = ListaPiezas.index(black[i])
        if black[i] == 'peon' :
            screen.blit(peonNegro, (blackPlaces[i][0] * 100 + 22, blackPlaces [i] [1]* 100 +30))
        else:
            screen.blit(imagenesNegras[index], (blackPlaces[i][0] * 100 + 10, blackPlaces [i] [1]* 100 +10))




#juego principal
run = True
while run:
    timer.tick(fps)
    screen.fill('pink')
    tablero()
    Piezas()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    
    pygame.display.flip 
    pygame.display.update()
pygame.quit()
