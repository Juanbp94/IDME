import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])  # screen
pygame.display.set_caption('1vs1 Ajedrez')  # Two-Player Pygame Chess!
fuente = pygame.font.Font('freesansbold.ttf', 20)  # font
fuenteMediana = pygame.font.Font('freesansbold.ttf', 40)  # medium_font
fuenteGrande = pygame.font.Font('freesansbold.ttf', 50)  # big_font
temporizador = pygame.time.Clock()  # timer
fps = 60
# variables y imágenes del juego
piezasBlancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']  # white_pieces
zonaBlancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]  # white_locations
piezasNegras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']  # black_pieces
zonaNegras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]  # black_locations
comidasBlancas = []  # captured_pieces_white
comidasNegras = []  # captured_pieces_black
# 0 - turno de blancas sin selección: 1- turno de blancas pieza seleccionada: 2- turno de negras sin selección, 3 - turno de negras pieza seleccionada
pasoTurno = 0  # turn_step
seleccion = 100  # selection
movimientosValidos = []  # valid_moves
# carga las imágenes de las piezas del juego (reina, rey, torre, alfil, caballo, peón) x 2

reinaNegra = pygame.image.load('imagenes/reina_negras.png')  # black_queen
reinaNegra = pygame.transform.scale(reinaNegra, (80, 80))
reinaNegraPeque = pygame.transform.scale(reinaNegra, (45, 45))  # black_queen_small
reyNegra = pygame.image.load('imagenes/rey_negras.png')  # black_king
reyNegra = pygame.transform.scale(reyNegra, (80, 80))
reyNegroPeque = pygame.transform.scale(reyNegra, (45, 45))  # black_king_small
torreNegra = pygame.image.load('imagenes/torre_negras.png')  # black_rook
torreNegra = pygame.transform.scale(torreNegra, (80, 80))
torreNegraPeque = pygame.transform.scale(torreNegra, (45, 45))  # black_rook_small
alfilNegra = pygame.image.load('imagenes/alfil_negras.png')  # black_bishop
alfilNegra = pygame.transform.scale(alfilNegra, (80, 80))
alfilNegraPeque = pygame.transform.scale(alfilNegra, (45, 45))  # black_bishop_small
caballoNegra = pygame.image.load('imagenes/caballo_negras.png')  # black_knight
caballoNegra = pygame.transform.scale(caballoNegra, (80, 80))
caballoNegraPeque = pygame.transform.scale(caballoNegra, (45, 45))  # black_knight_small
peonNegra = pygame.image.load('imagenes/peon_negras.png')  # black_pawn
peonNegra = pygame.transform.scale(peonNegra, (65, 65))
peonNegraPeque = pygame.transform.scale(peonNegra, (45, 45))  # black_pawn_small
reinaBlanca = pygame.image.load('imagenes/reina_blancas.png')  # white_queen
reinaBlanca = pygame.transform.scale(reinaBlanca, (80, 80))
reinaBlancaPeque = pygame.transform.scale(reinaBlanca, (45, 45))  # white_queen_small
reyBlanca = pygame.image.load('imagenes/rey_blancas.png')  # white_king
reyBlanca = pygame.transform.scale(reyBlanca, (80, 80))
reyBlancaPeque = pygame.transform.scale(reyBlanca, (45, 45))  # white_king_small
torreBlanca = pygame.image.load('imagenes/torre_blancas.png')  # white_rook
torreBlanca = pygame.transform.scale(torreBlanca, (80, 80))
torreBlancaPeque = pygame.transform.scale(torreBlanca, (45, 45))  # white_rook_small
alfilBlanca = pygame.image.load('imagenes/alfil_blancas.png')  # white_bishop
alfilBlanca = pygame.transform.scale(alfilBlanca, (80, 80))
alfilBlancaPeque = pygame.transform.scale(alfilBlanca, (45, 45))  # white_bishop_small
caballoBlanca = pygame.image.load('imagenes/caballo_blancas.png')  # white_knight
caballoBlanca = pygame.transform.scale(caballoBlanca, (80, 80))
caballoBlancaPeque = pygame.transform.scale(caballoBlanca, (45, 45))  # white_knight_small
peonBlanca = pygame.image.load('imagenes/peon_blancas.png')  # white_pawn
peonBlanca = pygame.transform.scale(peonBlanca, (65, 65))
peonBlancaPeque = pygame.transform.scale(peonBlanca, (45, 45))  # white_pawn_small
imagenesBlancas = [peonBlanca, reinaBlanca, reyBlanca, caballoBlanca, torreBlanca, alfilBlanca]  # white_images
imagenesBlancasPeque = [peonBlancaPeque, reinaBlancaPeque, reyBlancaPeque, caballoBlancaPeque,
                      torreBlancaPeque, alfilBlancaPeque]  # small_white_images
imagenesNegras = [peonNegra, reinaNegra, reyNegra, caballoNegra, torreNegra, alfilNegra]  # black_images
imagenesNegrasPeque = [peonNegraPeque, reinaNegraPeque, reyNegroPeque, caballoNegraPeque,
                      torreNegraPeque, alfilNegraPeque]  # small_black_images
listaPiezas = ['peon', 'reina', 'rey', 'caballo', 'torre', 'alfil']  # piece_list


# variables/ contador de parpadeo
contador = 0  # counter
ganador = ''  # winner
gameOver = False  # game_over


# dibuja el tablero principal del juego
def tablero():  # draw_board
    for i in range(32):
        columna = i % 4  # column
        fila = i // 4  # row
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, 'light gray', [600 - (columna * 200), fila * 100, 100, 100])
        else:
            pygame.draw.rect(pantalla, 'light gray', [700 - (columna * 200), fila * 100, 100, 100])
        pygame.draw.rect(pantalla, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(pantalla, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(pantalla, 'gold', [800, 0, 200, HEIGHT], 5)
        texto = ['Blancas: ¡Selecciona una pieza para mover!', 'Blancas: ¡Selecciona un destino!',
                       'Negras: ¡Selecciona una pieza para mover!', 'Negras: ¡Selecciona un destino!']  # status_text
        pantalla.blit(fuenteGrande.render(texto[pasoTurno], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(pantalla, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(pantalla, 'black', (100 * i, 0), (100 * i, 800), 2)
        pantalla.blit(fuenteMediana.render('RENDIRSE', True, 'black'), (810, 830))  # FORFEIT


# dibuja las piezas en el tablero
def colocaPiezas():  # draw_pieces
    for i in range(len(piezasBlancas)):  # white_pieces
        indicePiezas = listaPiezas.index(piezasBlancas[i])  # piece_list
        if piezasBlancas[i] == 'peon':  # pawn
            pantalla.blit(peonBlanca, (zonaBlancas[i][0] * 100 + 22, zonaBlancas[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesBlancas[indicePiezas], (zonaBlancas[i][0] * 100 + 10, zonaBlancas[i][1] * 100 + 10))
        if pasoTurno < 2:
            if seleccion == i:
                pygame.draw.rect(pantalla, 'red', [zonaBlancas[i][0] * 100 + 1, zonaBlancas[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(piezasNegras)):  # black_pieces
        indicePiezas = listaPiezas.index(piezasNegras[i])  # piece_list
        if piezasNegras[i] == 'peon':  # pawn
            pantalla.blit(peonNegra, (zonaNegras[i][0] * 100 + 22, zonaNegras[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesNegras[indicePiezas], (zonaNegras[i][0] * 100 + 10, zonaNegras[i][1] * 100 + 10))
        if pasoTurno >= 2:  # turn_step
            if seleccion == i:
                pygame.draw.rect(pantalla, 'blue', [zonaNegras[i][0] * 100 + 1, zonaNegras[i][1] * 100 + 1,
                                                100, 100], 2)


# función para comprobar todas las opciones válidas de las piezas en el tablero
def opcionesValidas(piezas, lugar, turno):  # check_options
    listaMovimientos = []  # moves_list
    ListaTodosMovimientos = []  # all_moves_list
    for i in range((len(piezas))):
        posicion = lugar[i]  # location
        pieza = piezas[i]  # piece
        if pieza == 'peon':  # pawn
            listaMovimientos = revisaPeon(posicion, turno)  # check_pawn
        elif pieza == 'torre':  # rook
            listaMovimientos = revisaTorre(posicion, turno)  # check_rook
        elif pieza == 'caballo':  # knight
            listaMovimientos = revisaCaballo(posicion, turno)  # check_knight
        elif pieza == 'alfil':  # bishop
            listaMovimientos = revisaAlfil(posicion, turno)  # check_bishop
        elif pieza == 'reina':  # queen
            listaMovimientos = revisaReina(posicion, turno)  # check_queen
        elif pieza == 'rey':  # king
            listaMovimientos = revisaRey(posicion, turno)  # check_king
        ListaTodosMovimientos.append(listaMovimientos)
    return ListaTodosMovimientos


# comprobar movimientos válidos del rey
def revisaRey(posicion, color):  # check_king
    listaMovimientos = []  # moves_list
    if color == 'blancas':  # white
        listaEnemiga = zonaNegras  # black_locations
        ListaAliados = zonaBlancas  # white_locations
    else:
        ListaAliados = zonaNegras  # black_locations
        listaEnemiga = zonaBlancas  # white_locations
    # 8 casillas para comprobar para los reyes, pueden ir una casilla en cualquier dirección
    moviRey = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]  # targets
    for i in range(8):
        objetivo = (posicion[0] + moviRey[i][0], posicion[1] + moviRey[i][1])  # target
        if objetivo not in ListaAliados and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            listaMovimientos.append(objetivo)
    return listaMovimientos


# comprobar movimientos válidos de la reina
def revisaReina(posicion, color):  # check_queen
    listaMovimientos = revisaAlfil(posicion, color)  # check_bishop
    segundaLista = revisaTorre(posicion, color)  # check_rook
    for i in range(len(segundaLista)):
        listaMovimientos.append(segundaLista[i])
    return listaMovimientos


# comprobar movimientos del alfil
def revisaAlfil(posicion, color):  # check_bishop
    listaMovimientos = []  # moves_list
    if color == 'blancas':  # white
        listaEnemiga = zonaNegras  # black_locations
        ListaAliados = zonaBlancas  # white_locations
    else:
        ListaAliados = zonaNegras  # black_locations
        listaEnemiga = zonaBlancas  # white_locations
    for i in range(4):  # arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda
        comoAlfil = True  # path
        cuantoAlfil = 1  # chain
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while comoAlfil:
            if (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)) not in ListaAliados and \
                    0 <= posicion[0] + (cuantoAlfil * x) <= 7 and 0 <= posicion[1] + (cuantoAlfil * y) <= 7:
                listaMovimientos.append((posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)))
                if (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)) in listaEnemiga:
                    comoAlfil = False
                cuantoAlfil += 1
            else:
                comoAlfil = False
    return listaMovimientos


# comprobar movimientos de la torre
def revisaTorre(posicion, color):  # check_rook
    listaMovimientos = []  # moves_list
    if color == 'blancas':  # white
        listaEnemiga = zonaNegras  # black_locations
        ListaAliados = zonaBlancas  # white_locations
    else:
        ListaAliados = zonaNegras  # black_locations
        listaEnemiga = zonaBlancas  # white_locations
    for i in range(4):  # abajo, arriba, derecha, izquierda
        comoAlfil = True  # path
        cuantoAlfil = 1  # chain
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while comoAlfil:
            if (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)) not in ListaAliados and \
                    0 <= posicion[0] + (cuantoAlfil * x) <= 7 and 0 <= posicion[1] + (cuantoAlfil * y) <= 7:
                listaMovimientos.append((posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)))
                if (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y)) in listaEnemiga:
                    comoAlfil = False
                cuantoAlfil += 1
            else:
                comoAlfil = False
    return listaMovimientos


def revisaPeon(posicion, color):  # check_pawn
    listaMovimientos = []  # moves_list
    if color == 'blancas':  # white
        if (posicion[0], posicion[1] + 1) not in zonaBlancas and  (posicion[0], posicion[1] + 1) not in zonaNegras and posicion[1] < 7:
            listaMovimientos.append((posicion[0], posicion[1] + 1))
        if (posicion[0], posicion[1] + 2) not in zonaBlancas and (posicion[0], posicion[1] + 2) not in zonaNegras and posicion[1] == 1:
            listaMovimientos.append((posicion[0], posicion[1] + 2))
        if (posicion[0] + 1, posicion[1] + 1) in zonaNegras:
            listaMovimientos.append((posicion[0] + 1, posicion[1] + 1))
        if (posicion[0] - 1, posicion[1] + 1) in zonaNegras:
            listaMovimientos.append((posicion[0] - 1, posicion[1] + 1))
    else:
        if (posicion[0], posicion[1] - 1) not in zonaBlancas and (posicion[0], posicion[1] - 1) not in zonaNegras and posicion[1] > 0:
            listaMovimientos.append((posicion[0], posicion[1] - 1))
        if (posicion[0], posicion[1] - 2) not in zonaBlancas and (posicion[0], posicion[1] - 2) not in zonaNegras and posicion[1] == 6:
            listaMovimientos.append((posicion[0], posicion[1] - 2))
        if (posicion[0] + 1, posicion[1] - 1) in zonaBlancas:
            listaMovimientos.append((posicion[0] + 1, posicion[1] - 1))
        if (posicion[0] - 1, posicion[1] - 1) in zonaBlancas:
            listaMovimientos.append((posicion[0] - 1, posicion[1] - 1))
    return listaMovimientos




# comprobar los movimientos válidos solo para la pieza seleccionada
def movimientoValido():  # check_valid_moves
    if pasoTurno < 2:  # turn_step
        listaOpciones = opcionesBlancas  # white_options
    else:
        listaOpciones = opcionesNegras  # black_options
    opcionesValidas = listaOpciones[seleccion]  # valid_options
    return opcionesValidas
 

# dibuja las piezas capturadas en el lateral de la pantalla
def capturadas():  # draw_captured
    for i in range(len(comidasBlancas)):  # captured_pieces_white
        piezaCapturada = comidasBlancas[i]  # captured_piece
        indicePiezas = listaPiezas.index(piezaCapturada)  # piece_list
        pantalla.blit(imagenesNegrasPeque[indicePiezas], (825, 5 + 50 * i))
    for i in range(len(comidasNegras)):  # captured_pieces_black
        piezaCapturada = comidasNegras[i]  # captured_piece
        indicePiezas = listaPiezas.index(piezaCapturada)  # piece_list
        pantalla.blit(imagenesBlancasPeque[indicePiezas], (925, 5 + 50 * i))


# dibuja un cuadrado parpadeante alrededor del rey si está en jaque
def jaque():  # draw_check
    if pasoTurno < 2:  # turn_step
        if 'rey' in piezasBlancas:  # white_pieces
            indiceRey = piezasBlancas.index('rey')  # king_index
            ubicacionRey = zonaBlancas[indiceRey]  # king_location
            for i in range(len(opcionesNegras)):  # black_options
                if ubicacionRey in opcionesNegras[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                                zonaBlancas[indiceRey][1] * 100 + 1,
                                                                100, 100], 2)
                    else:
                        pygame.draw.rect(pantalla, 'red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                            zonaBlancas[indiceRey][1] * 100 + 1,
                                                            100, 100], 2)
    else:
        if 'rey' in piezasNegras:  # black_pieces
            indiceRey = piezasNegras.index('rey')  # king_index
            ubicacionRey = zonaNegras[indiceRey]  # king_location
            for i in range(len(opcionesBlancas)):  # white_options
                if ubicacionRey in opcionesBlancas[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark blue', [zonaNegras[indiceRey][0] * 100 + 1,
                                                                zonaNegras[indiceRey][1] * 100 + 1,
                                                                100, 100], 2)
                    else:
                        pygame.draw.rect(pantalla, 'blue', [zonaNegras[indiceRey][0] * 100 + 1,
                                                            zonaNegras[indiceRey][1] * 100 + 1,
                                                            100, 100], 2)



# comprobar movimientos válidos del caballo
def revisaCaballo(posicion, color):  # check_knight
    listaMovimientos = []  # moves_list
    if color == 'blancas':  # white
        listaEnemiga = zonaNegras  # black_locations
        ListaAliados = zonaBlancas  # white_locations
    else:
        ListaAliados = zonaNegras  # black_locations
        listaEnemiga = zonaBlancas  # white_locations
    # 8 casillas para comprobar para los caballos, pueden ir dos casillas en una dirección y una en otra
    moviRey = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]  # targets
    for i in range(8):
        objetivo = (posicion[0] + moviRey[i][0], posicion[1] + moviRey[i][1])  # target
        if objetivo not in ListaAliados and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            listaMovimientos.append(objetivo)
    return listaMovimientos


# dibuja los movimientos válidos en la pantalla
def Valido(movimientos):  # draw_valid
    if pasoTurno < 2:  # turn_step
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(movimientos)):
        pygame.draw.circle(pantalla, color, (movimientos[i][0] * 100 + 50, movimientos[i][1] * 100 + 50), 5)


# dibuja un cuadrado parpadeante alrededor del rey si está en jaque
def jaque():  # draw_check
    if pasoTurno < 2:  # turn_step
        if 'rey' in piezasBlancas:  # white_pieces
            indiceRey = piezasBlancas.index('rey')  # king_index
            ubicacionRey = zonaBlancas[indiceRey]  # king_location
            for i in range(len(opcionesNegras)):  # black_options
                if ubicacionRey in opcionesNegras[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                                zonaBlancas[indiceRey][1] * 100 + 1,
                                                                100, 100], 2)
                    else:
                        pygame.draw.rect(pantalla, 'red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                            zonaBlancas[indiceRey][1] * 100 + 1,
                                                            100, 100], 2)
    else:
        if 'rey' in piezasNegras:  # black_pieces
            indiceRey = piezasNegras.index('rey')  # king_index
            ubicacionRey = zonaNegras[indiceRey]  # king_location
            for i in range(len(opcionesBlancas)):  # white_options
                if ubicacionRey in opcionesBlancas[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark blue', [zonaNegras[indiceRey][0] * 100 + 1,
                                                                zonaNegras[indiceRey][1] * 100 + 1,
                                                                100, 100], 2)
                    else:
                        pygame.draw.rect(pantalla, 'blue', [zonaNegras[indiceRey][0] * 100 + 1,
                                                            zonaNegras[indiceRey][1] * 100 + 1,
                                                            100, 100], 2)


def dibujaFinDeJuego():  # draw_game_over
    pygame.draw.rect(pantalla, 'black', [200, 200, 400, 70])
    pantalla.blit(fuente.render(f'{ganador} ganó la partida!', True, 'white'), (210, 210))  # {winner} won the game!
    pantalla.blit(fuente.render(f'¡Presiona ENTER para reiniciar!', True, 'white'), (210, 240))  # Press ENTER to Restart!


# bucle principal del juego
opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  # black_options
opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  # white_options
empieza = True  # run
while empieza:  # run
    temporizador.tick(fps)  # timer
    if contador < 30:
        contador += 1
    else:
        contador = 0
    pantalla.fill('dark gray')
    tablero()  # draw_board
    colocaPiezas()  # draw_pieces
    capturadas()  # draw_captured
    jaque()  # draw_check
    if seleccion != 100:
        movimientosValidos = movimientoValido()  # check_valid_moves
        Valido(movimientosValidos)  # draw_valid
    # manejo de eventos
    for evento in pygame.event.get():  # event
        if evento.type == pygame.QUIT:  # event.type == pygame.QUIT
            empieza = False  # run
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not gameOver:
            coordenadaX = evento.pos[0] // 100  # x_coord
            coordenadaY = evento.pos[1] // 100  # y_coord
            clickCoordenadas = (coordenadaX, coordenadaY)  # click_coords
            if pasoTurno <= 1:
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'negras'  # black
                if clickCoordenadas in zonaBlancas:
                    seleccion = zonaBlancas.index(clickCoordenadas)
                    if pasoTurno == 0:
                        pasoTurno = 1
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaBlancas[seleccion] = clickCoordenadas
                    if clickCoordenadas in zonaNegras:
                        piezaNegra = zonaNegras.index(clickCoordenadas)
                        comidasBlancas.append(piezasNegras[piezaNegra])
                        if piezasNegras[piezaNegra] == 'rey':
                            ganador = 'blancas'  
                        piezasNegras.pop(piezaNegra)
                        zonaNegras.pop(piezaNegra)
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  # black_options
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  # white_options
                    pasoTurno = 2
                    seleccion = 100
                    movimientosValidos = []
            if pasoTurno > 1:
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'blancas'  # white
                if clickCoordenadas in zonaNegras:
                    seleccion = zonaNegras.index(clickCoordenadas)
                    if pasoTurno == 2:
                        pasoTurno = 3
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaNegras[seleccion] = clickCoordenadas
                    if clickCoordenadas in zonaBlancas:
                        piezaBlanca = zonaBlancas.index(clickCoordenadas)
                        comidasNegras.append(piezasBlancas[piezaBlanca])
                        if piezasBlancas[piezaBlanca] == 'rey':
                            ganador = 'negras'  # black
                        piezasBlancas.pop(piezaBlanca)
                        zonaBlancas.pop(piezaBlanca)
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  # black_options
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  # white_options
                    pasoTurno = 0
                    seleccion = 100
                    movimientosValidos = []
        if evento.type == pygame.KEYDOWN and gameOver:
            if evento.key == pygame.K_RETURN:
                gameOver = False
                ganador = ''
                piezasBlancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                zonaBlancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                piezasNegras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                zonaNegras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                comidasBlancas = []
                comidasNegras = []
                pasoTurno = 0
                seleccion = 100
                movimientosValidos = []
                opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  # black_options
                opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  # white_options

    if ganador != '':
        gameOver = True
        dibujaFinDeJuego()  # draw_game_over

    pygame.display.flip()
pygame.quit()



