
# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
reinaBlanca = pygame.image.load('ajedrez/juego/imagenes/reinab.png')
reinaBlanca = pygame.transform.scale(reinaBlanca, (80,80))
reinaBlancaPeque = pygame.transform.scale(reinaBlanca, (45,45))
reyBlanco = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/reyb.png')
reyBlanco = pygame.transform.scale(reyBlanco, (80, 80))
reyBlancoPeque = pygame.transform.scale(reyBlanco, (45, 45))
torreBlanca = pygame.image.load('G:/Mi unidad/mantenimiento electronico/python/ajedrez/juego/imagenes/torreb.png')
torreBlancaPeque = pygame.transform.scale(torreBlanca, (80, 80))
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

ListaPiezas = ['peon', 'reina', 'rey', 'alfil', 'torre', 'caballo' ]
# check variables/ flashing counter



# main game loop

run = True
while run:
    timer.tick(fps)
    
    
    screen.fill('dark gray')

   

    if winner != '':
        game_over = True
        

    pygame.display.flip()
pygame.quit()
