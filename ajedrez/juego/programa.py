

import pygame

pygame.init()

WIDTH = 1500
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Ajedrez')
font = pygame.font.SysFont('Arial', 30)
big_font = pygame.font.SysFont('arial',50)
timer = pygame.time.Clock()
fps = 60

#piezas

white =['torre','caballo', 'alfil','rey', 'reina','alfil','caballo','torre',
           'peon','peon','peon','peon','peon','peon','peon','peon',]

white_places = [(0,0),(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                (0,1),(1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black =['torre','caballo', 'alfil','rey', 'reina','alfil','caballo','torre',
           'peon','peon','peon','peon','peon','peon','peon','peon',]
black_places = [(0,7),(1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                (0,6),(1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

comidas_blancas = []
comidas_negras = []
#0 - turno de blancas, sin seleccion --> 1 turno de blancas, con seleccion --> 2 turno de negras , sin seleccion --> 3 turno de negras con seleccion
paso_turno = 0
seleccion = 500
movimientos_validos = []

#imagenes de las piezas y escalado para el tablero (revisar tamaños segun pantalla)

reina_blanca = pygame.image.load('ajedrez/assets/imagenes/w_queen_png_1024px.png')
reina_blanca = pygame.transform.scale(reina_blanca, (80,80))
reina_blanca_peque = pygame.transform.scale(reina_blanca, (45,45))
rey_blanco = pygame.image.load('ajedrez/assets/imagenes/w_king_png_1024px.png')
rey_blanco = pygame.transform.scale(rey_blanco, (80, 80))
rey_blanco_small = pygame.transform.scale(rey_blanco, (45, 45))
torre_blanca = pygame.image.load('ajedrez/assets/imagenes/w_rook_png_1024px.png')
torre_blanca_small = pygame.transform.scale(torre_blanca, (80, 80))
torre_blanca_small = pygame.transform.scale(torre_blanca, (45, 45))
alfil_blanco = pygame.image.load('ajedrez/assets/imagenes/w_bishop_png_1024px.png')
alfil_blanco = pygame.transform.scale(alfil_blanco, (80, 80))
alfil_blanco_small = pygame.transform.scale(alfil_blanco, (45, 45))
caballo_blanco = pygame.image.load('ajedrez/assets/imagenes/w_knight_png_1024px.png')
caballo_blanco = pygame.transform.scale(caballo_blanco, (80, 80))
caballo_blanco_small = pygame.transform.scale(caballo_blanco, (45, 45))
peon_blanco = pygame.image.load('ajedrez/assets/imagenes/w_pawn_png_1024px.png')
peon_blanco = pygame.transform.scale(peon_blanco, (65, 65))
peon_blanco_small = pygame.transform.scale(peon_blanco, (45, 45))

reina_negra = pygame.image.load('ajedrez/assets/imagenes/b_queen_png_1024px.png')
reina_negra = pygame.transform.scale(reina_negra, (80, 80))
reina_negra_small = pygame.transform.scale(reina_negra, (45, 45))
rey_negro = pygame.image.load('ajedrez/assets/imagenes/b_king_png_1024px.png')
rey_negro = pygame.transform.scale(rey_negro, (80, 80))
rey_negro_small = pygame.transform.scale(rey_negro, (45, 45))
torre_negra = pygame.image.load('ajedrez/assets/imagenes/b_rook_png_1024px.png')
torre_negra = pygame.transform.scale(torre_negra, (80, 80))
torre_negra_small = pygame.transform.scale(torre_negra, (45, 45))
alfil_negro = pygame.image.load('ajedrez\assets\imagenes\b_bishop_png_1024px.png')
alfil_negro = pygame.transform.scale(alfil_negro, (80, 80))
alfil_negro_small = pygame.transform.scale(alfil_negro, (45, 45))
caballo_negro = pygame.image.load('ajedrez/assets/imagenes/b_knight_png_1024px.png')
caballo_negro = pygame.transform.scale(caballo_negro, (80, 80))
caballo_negro_small = pygame.transform.scale(caballo_negro, (45, 45))
peon_negro = pygame.image.load('ajedrez/assets/imagenes/b_pawn_png_1024px.png')
peon_negro = pygame.transform.scale(peon_negro, (65, 65))
peon_negro_small = pygame.transform.scale(peon_negro, (45, 45))



run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    
    pygame.display.flip 
pygame.quit()
