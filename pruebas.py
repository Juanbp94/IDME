
import pygame

#Se inicia el juego
pygame.init()
#Tamaño de la ventana
WIDTH = 1000
HEIGHT = 900
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])  # Creacion de la ventana
temporizador = pygame.time.Clock() 
fps=60
fuente = pygame.font.SysFont('Arial.ttf', 30) # fuente
fuenteMediana = pygame.font.SysFont('Arial.ttf', 40)  
fuenteGrande = pygame.font.SysFont('Arial.ttf', 50)  


# ---------- MENÚ PRINCIPAL ----------

# Crea la pantalla
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajedrez 1 vs 1")

# Carga la imagen de fondo
fondoMenu = pygame.image.load('imagenes/fondo.jpg')
fondoMenu = pygame.transform.scale(fondoMenu, (WIDTH, HEIGHT))

# Inputs para los nombres de los jugadores
jugador1 = ""
jugador2 = ""
activoJugador1 = False
activoJugador2 = False

# Define los colores para los inputs
colorInputInactivo = pygame.Color('darkgoldenrod1')
colorInputActivo = pygame.Color('chartreuse')
colorInput1 = colorInputInactivo
colorInput2 = colorInputInactivo

# Define las fuentes para el texto
fuenteInput = pygame.font.SysFont('Arial', 40)
botonFuente = pygame.font.SysFont('Arial', 50)

# Define la variable para controlar si la partida ha comenzado
iniciarPartida = False

# Define los rectángulos para los inputs y el botón
rectInput1 = pygame.Rect(350, 300, 300, 50)
rectInput2 = pygame.Rect(350, 400, 300, 50)
botonIniciar = pygame.Rect(400, 520, 200, 60)

# Bucle principal del menú
while not iniciarPartida:
    # Obtiene los eventos del teclado y el ratón
    for evento in pygame.event.get():
        # Si se cierra la ventana, termina el programa
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Si se hace clic con el ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Si se hace clic en el input del jugador 1
            if rectInput1.collidepoint(evento.pos):
                activoJugador1 = True
                activoJugador2 = False
            # Si se hace clic en el input del jugador 2
            elif rectInput2.collidepoint(evento.pos):
                activoJugador1 = False
                activoJugador2 = True
            # Si se hace clic en el botón "Iniciar"
            elif botonIniciar.collidepoint(evento.pos):
                # Si se han introducido los nombres de los jugadores, elimina los espacios en blanco (evita graciosos)
                if jugador1.strip() and jugador2.strip():
                    # Comienza la partida
                    iniciarPartida = True
                    # Establece el título de la ventana
                    pygame.display.set_caption(f'{jugador1} vs {jugador2}')
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si el input del jugador 1 está activo
            if activoJugador1:
                # Si se presiona la tecla "Backspace"
                if evento.key == pygame.K_BACKSPACE:
                    # Elimina el último carácter del nombre del jugador 1
                    jugador1 = jugador1[:-1]
                # Si se presiona otra tecla
                else:
                    # Añade el carácter al nombre del jugador 1
                    jugador1 += evento.unicode
            # Si el input del jugador 2 está activo
            elif activoJugador2:
                # Si se presiona la tecla "Backspace"
                if evento.key == pygame.K_BACKSPACE:
                    # Elimina el último carácter del nombre del jugador 2
                    jugador2 = jugador2[:-1]
                # Si se presiona otra tecla
                else:
                    # Añade el carácter al nombre del jugador 2
                    jugador2 += evento.unicode

    # Actualiza el color de los inputs según estén activos o no
    colorInput1 = colorInputActivo if activoJugador1 else colorInputInactivo
    colorInput2 = colorInputActivo if activoJugador2 else colorInputInactivo

    # Dibuja el fondo
    pantalla.blit(fondoMenu, (0, 0))

    # Dibuja el título del menú
    titulo = botonFuente.render("AJEDREZ 1 VS 1", True, 'darkolivegreen1')
    pantalla.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 150))

    # Dibuja los cuadros de texto para los inputs
    pygame.draw.rect(pantalla, colorInput1, rectInput1, 2)
    pygame.draw.rect(pantalla, colorInput2, rectInput2, 2)

    # Dibuja el texto de los inputs
    textoInput1 = fuenteInput.render(jugador1, True, 'deepskyblue')
    textoInput2 = fuenteInput.render(jugador2, True, 'deepskyblue')

    pantalla.blit(textoInput1, (rectInput1.x + 10, rectInput1.y + 10))
    pantalla.blit(textoInput2, (rectInput2.x + 10, rectInput2.y + 10))

    # Dibuja las etiquetas de los inputs
    pantalla.blit(fuenteInput.render("Jugador 1:", True, 'white'), (rectInput1.x - 160, rectInput1.y + 10))
    pantalla.blit(fuenteInput.render("Jugador 2:", True, 'white'), (rectInput2.x - 160, rectInput2.y + 10))

    # Dibuja el botón "Iniciar"
    pygame.draw.rect(pantalla, 'gold', botonIniciar)
    pantalla.blit(botonFuente.render("INICIAR", True, 'black'), (botonIniciar.x + 25, botonIniciar.y + 10))

    # Actualiza la pantalla
    pygame.display.flip()
    
  
#
with open("movimientos.txt", "w") as archivo: # borra el txt al iniciar cada partida 
    archivo.write("  ")
# variables y imágenes del juego
piezasBlancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']  # Piezas blancas
zonaBlancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]  # donde van las blancas (parte de arriba)
piezasNegras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']  # piezas negras
zonaNegras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]  # donde van las negras (parte de abajo)
comidasBlancas = []  # ariable que guarda las piezaxs comidas
comidasNegras = []  # variable que guarda las piezaxs comidas
# 0 - turno de blancas sin selección: 1- turno de blancas pieza seleccionada: 2- turno de negras sin selección, 3 - turno de negras pieza seleccionada
pasoTurno = 0  # paso turno
seleccion = 100  # parametro para controlar la seleccion de piezas
movimientosValidos = []  # movimientos validos
# carga las imágenes de las piezas del juego (reina, rey, torre, alfil, caballo, peón) x 2

def cargar_imagen(nombre_archivo, tamaño):
    """Carga una imagen y la escala al tamaño especificado.
        nombre_archivo (str): El nombre del archivo de la imagen.
        tamaño (tupla): Una tupla con el ancho y alto deseado de la imagen.
    Returns:
        pygame.Surface: La imagen cargada y escalada.
    """
    imagen = pygame.image.load(nombre_archivo)
    imagen = pygame.transform.scale(imagen, tamaño)
    return imagen
# Carga las imágenes de las piezas
reinaNegra = cargar_imagen('imagenes/reina_negras.png', (80, 80))
reinaNegraPeque = cargar_imagen('imagenes/reina_negras.png', (45, 45))
reyNegra = cargar_imagen('imagenes/rey_negras.png', (80, 80))
reyNegroPeque = cargar_imagen('imagenes/rey_negras.png', (45, 45))
torreNegra = cargar_imagen('imagenes/torre_negras.png', (80, 80))
torreNegraPeque = cargar_imagen('imagenes/torre_negras.png', (45, 45))
caballoNegra = cargar_imagen('imagenes/caballo_negras.png', (80, 80))
caballoNegraPeque = cargar_imagen('imagenes/caballo_negras.png', (45, 45))
alfilNegra = cargar_imagen('imagenes/alfil_negras.png', (80, 80))
alfilNegraPeque = cargar_imagen('imagenes/alfil_negras.png', (45, 45))
peonNegra = cargar_imagen('imagenes/peon_negras.png', (65, 65))
peonNegraPeque = cargar_imagen('imagenes/peon_negras.png', (45, 45))

reinaBlanca = cargar_imagen('imagenes/reina_blancas.png', (80, 80))
reinaBlancaPeque = cargar_imagen('imagenes/reina_blancas.png', (45, 45))
reyBlanca = cargar_imagen('imagenes/rey_blancas.png', (80, 80))
reyBlancaPeque = cargar_imagen('imagenes/rey_blancas.png', (45, 45))
torreBlanca = cargar_imagen('imagenes/torre_blancas.png', (80, 80))
torreBlancaPeque = cargar_imagen('imagenes/torre_blancas.png', (45, 45))
caballoBlanca = cargar_imagen('imagenes/caballo_blancas.png', (80, 80))
caballoBlancaPeque = cargar_imagen('imagenes/caballo_blancas.png', (45, 45))
alfilBlanca = cargar_imagen('imagenes/alfil_blancas.png', (80, 80))
alfilBlancaPeque = cargar_imagen('imagenes/alfil_blancas.png', (45, 45))
peonBlanca = cargar_imagen('imagenes/peon_blancas.png', (65, 65))
peonBlancaPeque = cargar_imagen('imagenes/peon_blancas.png', (45, 45))
imagenesBlancas = [peonBlanca, reinaBlanca, reyBlanca, caballoBlanca, torreBlanca, alfilBlanca]  
imagenesBlancasPeque = [peonBlancaPeque, reinaBlancaPeque, reyBlancaPeque, caballoBlancaPeque,
                      torreBlancaPeque, alfilBlancaPeque]  
imagenesNegras = [peonNegra, reinaNegra, reyNegra, caballoNegra, torreNegra, alfilNegra]  #
imagenesNegrasPeque = [peonNegraPeque, reinaNegraPeque, reyNegroPeque, caballoNegraPeque,
                      torreNegraPeque, alfilNegraPeque]  
listaPiezas = ['peon', 'reina', 'rey', 'caballo', 'torre', 'alfil']  

# variables
contador = 0  
ganador = ''  
gameOver = False  

# dibuja el tablero principal del juego
def tablero():  
    for i in range(32):
        columna = i % 4  # columna
        fila = i // 4  # fila
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, 'whitesmoke', [600 - (columna * 200), fila * 100, 100, 100]) #colrea los cuadrantes centrales 
        else:
            pygame.draw.rect(pantalla, 'whitesmoke', [700 - (columna * 200), fila * 100, 100, 100])
        pygame.draw.rect(pantalla, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(pantalla, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(pantalla, 'gold', [800, 0, 200, HEIGHT], 5)
        texto = [f'{jugador1}: ¡Selecciona una pieza para mover!',
         f'{jugador1}: ¡Selecciona un destino!',
         f'{jugador2}: ¡Selecciona una pieza para mover!',
         f'{jugador2}: ¡Selecciona un destino!']  # texto del cuadrado inferior
        pantalla.blit(fuenteGrande.render(texto[pasoTurno], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(pantalla, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(pantalla, 'black', (100 * i, 0), (100 * i, 800), 2)
        pantalla.blit(fuenteMediana.render('RENDIRSE', True, 'black'), (810, 830))  # rendirse

# dibuja las piezas en el tablero
def colocaPiezas():  
    for i in range(len(piezasBlancas)):  # coloca las piezas blancas en su parte del tablero
        indicePiezas = listaPiezas.index(piezasBlancas[i])  
        if piezasBlancas[i] == 'peon':  
            pantalla.blit(peonBlanca, (zonaBlancas[i][0] * 100 + 22, zonaBlancas[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesBlancas[indicePiezas], (zonaBlancas[i][0] * 100 + 10, zonaBlancas[i][1] * 100 + 10))
        if pasoTurno < 2:
            if seleccion == i:
                pygame.draw.rect(pantalla, 'red', [zonaBlancas[i][0] * 100 + 1, zonaBlancas[i][1] * 100 + 1,
                                                 100, 100], 2) # colorea de rojo las piezas negras al seleccionarlas

    for i in range(len(piezasNegras)):  # coloca las piezas negras en su parte del tablero
        indicePiezas = listaPiezas.index(piezasNegras[i])  
        if piezasNegras[i] == 'peon':  
            pantalla.blit(peonNegra, (zonaNegras[i][0] * 100 + 22, zonaNegras[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesNegras[indicePiezas], (zonaNegras[i][0] * 100 + 10, zonaNegras[i][1] * 100 + 10))
        if pasoTurno >= 2:  
            if seleccion == i:
                pygame.draw.rect(pantalla, 'green', [zonaNegras[i][0] * 100 + 1, zonaNegras[i][1] * 100 + 1,
                                                100, 100], 2) # colorea de verde las piezas negras al seleccionarlas


# función para comprobar todas las opciones válidas de las piezas en el tablero
def opcionesValidas(piezas, lugar, turno):  
    listaMovimientos = []  
    ListaTodosMovimientos = []  
    for i in range((len(piezas))):
        posicion = lugar[i]  
        pieza = piezas[i]  
        if pieza == 'peon':  
            listaMovimientos = revisaPeon(posicion, turno)  
        elif pieza == 'torre':  
            listaMovimientos = revisaTorre(posicion, turno)  
        elif pieza == 'caballo':  
            listaMovimientos = revisaCaballo(posicion, turno)  
        elif pieza == 'alfil':  
            listaMovimientos = revisaAlfil(posicion, turno)  
        elif pieza == 'reina':  
            listaMovimientos = revisaReina(posicion, turno)  
        elif pieza == 'rey':  
            listaMovimientos = revisaRey(posicion, turno)  
        ListaTodosMovimientos.append(listaMovimientos)
        if listaMovimientos:
            with open("movimientos.txt", "a") as archivo: # escribe los movimientos que se hacen en el documento
                archivo.write(f"Turno {turno}: {pieza} en {posicion} se mueve a {listaMovimientos[0]}\n")
    return ListaTodosMovimientos


# comprobar movimientos válidos del rey
def revisaRey(posicion, color):  
    listaMovimientos = []  
    if color == 'blancas':  
        listaEnemiga = zonaNegras  
        ListaAliados = zonaBlancas  
    else:
        ListaAliados = zonaNegras  
        listaEnemiga = zonaBlancas  
    # 8 casillas para comprobar para los reyes, pueden ir una casilla en cualquier dirección
    moviRey = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]  
        # Iterar sobre los 8 posibles movimientos del rey (en todas las direcciones)
    for i in range(8):
        # Calculamos la nueva posición del rey sumando la dirección correspondiente al movimiento
        objetivo = (posicion[0] + moviRey[i][0], posicion[1] + moviRey[i][1])  

        # Verificar si el movimiento es válido:
        # 1. El objetivo no debe estar ocupado por una pieza aliada
        # 2. El objetivo debe estar dentro de los límites del tablero (coordenadas entre 0 y 7)
        if objetivo not in ListaAliados and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            # Si el movimiento es válido, se agrega a la lista de movimientos posibles
            listaMovimientos.append(objetivo)
    
    # Devolver la lista de movimientos válidos para el rey
    return listaMovimientos

# movimientos genericos de torre,alfil y reina
def revisaMovimientoLineal(posicion, color, direcciones):
    # Lista que contendrá los movimientos válidos de la pieza
    listaMovimientos = []
    
    # Definir qué piezas son enemigas y cuáles son aliadas dependiendo del color de la pieza
    if color == 'blancas':
        listaEnemiga = zonaNegras   # Las piezas enemigas son las negras
        ListaAliados = zonaBlancas  # Las piezas aliadas son las blancas
    else:
        ListaAliados = zonaNegras   # Si es negras, las piezas aliadas son las negras
        listaEnemiga = zonaBlancas  # Las piezas enemigas son las blancas

    # Recorrer todas las direcciones posibles (por ejemplo: (1, 0) = derecha, (0, 1) = abajo)
    for direccion in direcciones:
        comoAlfil = True  #  controla si seguimos moviéndonos en esta dirección
        cuantoAlfil = 1  # Contador para los pasos que se van tomando en esta dirección (1, 2, 3, ...)
        
        # Descomponer la dirección en sus componentes x e y (por ejemplo: (1, 0) = x=1, y=0)
        x = direccion[0]
        y = direccion[1]

        # Bucle que continúa mientras "comoAlfil" sea True
        while comoAlfil:
            # Calcular la nueva posición sumando los pasos actuales a la posición inicial
            nuevaPosicion = (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y))

            # Verificar que la nueva posición esté dentro del tablero y que no haya piezas aliadas allí
            if nuevaPosicion not in ListaAliados and \
                    0 <= nuevaPosicion[0] <= 7 and 0 <= nuevaPosicion[1] <= 7:
                # Si es una casilla válida, agregarla a la lista de movimientos válidos
                listaMovimientos.append(nuevaPosicion)
                
                # Si la nueva posición tiene una pieza enemiga, se puede capturar, pero no podemos seguir más allá
                if nuevaPosicion in listaEnemiga:
                    comoAlfil = False  # Deja de moverse en esta dirección

                # Incrementa el contador para avanzar al siguiente paso en esa dirección
                cuantoAlfil += 1
            else:
                # Si encuentra una pieza aliada o sale del tablero, detiene el movimiento en esta

#movimientos de la torre
def revisaTorre(posicion, color):
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return revisaMovimientoLineal(posicion, color, direcciones)
#movimientos del alfil
def revisaAlfil(posicion, color):
    direcciones = [(1, -1), (-1, -1), (1, 1), (-1, 1)]
    return revisaMovimientoLineal(posicion, color, direcciones)
#movimientos de la reina (alfil+torre)
def revisaReina(posicion, color):
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    return revisaMovimientoLineal(posicion, color, direcciones)
#movimientos del peon
def revisaPeon(posicion, color):  
    listaMovimientos = []  
    if color == 'blancas':  
        if (posicion[0], posicion[1] + 1) not in zonaBlancas and  (posicion[0], posicion[1] + 1) not in zonaNegras and posicion[1] < 7:
            listaMovimientos.append((posicion[0], posicion[1] + 1))#movimiento 1 delante
        if (posicion[0], posicion[1] + 2) not in zonaBlancas and (posicion[0], posicion[1] + 2) not in zonaNegras and posicion[1] == 1:
            listaMovimientos.append((posicion[0], posicion[1] + 2))#movimiento 2 delante
        if (posicion[0] + 1, posicion[1] + 1) in zonaNegras:
            listaMovimientos.append((posicion[0] + 1, posicion[1] + 1))#movimiento diagonal derecha
        if (posicion[0] - 1, posicion[1] + 1) in zonaNegras:
            listaMovimientos.append((posicion[0] - 1, posicion[1] + 1))#movimiento diagonal izquierda
    else:
        if (posicion[0], posicion[1] - 1) not in zonaBlancas and (posicion[0], posicion[1] - 1) not in zonaNegras and posicion[1] > 0:
            listaMovimientos.append((posicion[0], posicion[1] - 1)) #movimiento 1 delante
        if (posicion[0], posicion[1] - 2) not in zonaBlancas and (posicion[0], posicion[1] - 2) not in zonaNegras and posicion[1] == 6:
            listaMovimientos.append((posicion[0], posicion[1] - 2))#movimiento 2 delante 
        if (posicion[0] + 1, posicion[1] - 1) in zonaBlancas:
            listaMovimientos.append((posicion[0] + 1, posicion[1] - 1))#movimiento diagonal derecha
        if (posicion[0] - 1, posicion[1] - 1) in zonaBlancas:
            listaMovimientos.append((posicion[0] - 1, posicion[1] - 1))#movimiento diagonal izquierda
    return listaMovimientos




# comprobar los movimientos válidos solo para la pieza seleccionada
def movimientoValido():  
    if pasoTurno < 2:  
        listaOpciones = opcionesBlancas 
    else:
        listaOpciones = opcionesNegras  
    opcionesValidas = listaOpciones[seleccion]  
    return opcionesValidas
 

# dibuja las piezas capturadas en el lateral de la pantalla
def capturadas():  
    for i in range(len(comidasBlancas)): 
        piezaCapturada = comidasBlancas[i]  
        indicePiezas = listaPiezas.index(piezaCapturada)  
        pantalla.blit(imagenesNegrasPeque[indicePiezas], (825, 5 + 50 * i))
    for i in range(len(comidasNegras)):  
        piezaCapturada = comidasNegras[i]  
        indicePiezas = listaPiezas.index(piezaCapturada)  
        pantalla.blit(imagenesBlancasPeque[indicePiezas], (925, 5 + 50 * i))


# dibuja un cuadrado parpadeante alrededor del rey si está en jaque
def jaque():  
    if pasoTurno < 2:  
        if 'rey' in piezasBlancas:  
            indiceRey = piezasBlancas.index('rey')  
            ubicacionRey = zonaBlancas[indiceRey]  
            for i in range(len(opcionesNegras)):  
                if ubicacionRey in opcionesNegras[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                                zonaBlancas[indiceRey][1] * 100 + 1,
                                                                100, 100], 4)
                    else:
                        pygame.draw.rect(pantalla, 'red', [zonaBlancas[indiceRey][0] * 100 + 1,
                                                            zonaBlancas[indiceRey][1] * 100 + 1,
                                                            100, 100], 4)
    else:
        if 'rey' in piezasNegras:  
            indiceRey = piezasNegras.index('rey')  
            ubicacionRey = zonaNegras[indiceRey]  
            for i in range(len(opcionesBlancas)):  
                if ubicacionRey in opcionesBlancas[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'violetred1', [zonaNegras[indiceRey][0] * 100 + 1,
                                                                zonaNegras[indiceRey][1] * 100 + 1,
                                                                100, 100], 4)
                    else:
                        pygame.draw.rect(pantalla, 'blue', [zonaNegras[indiceRey][0] * 100 + 1,
                                                            zonaNegras[indiceRey][1] * 100 + 1,
                                                            100, 100], 4)



# comprobar movimientos válidos del caballo
def revisaCaballo(posicion, color):  
    listaMovimientos = []  
    if color == 'blancas':  
        listaEnemiga = zonaNegras  
        ListaAliados = zonaBlancas  
    else:
        ListaAliados = zonaNegras  
        listaEnemiga = zonaBlancas  
    # 8 casillas para comprobar para los caballos, pueden ir dos casillas en una dirección y una en otra
    moviRey = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]  # targets
    for i in range(8):
        objetivo = (posicion[0] + moviRey[i][0], posicion[1] + moviRey[i][1])  # target
        if objetivo not in ListaAliados and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            listaMovimientos.append(objetivo)
    return listaMovimientos


# dibuja los movimientos válidos en la pantalla
def Valido(movimientos):  
    if pasoTurno < 2: 
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(movimientos)):
        pygame.draw.circle(pantalla, color, (movimientos[i][0] * 100 + 50, movimientos[i][1] * 100 + 50), 5)





def dibujaFinDeJuego():  # draw_game_over
    pygame.draw.rect(pantalla, 'black', [200, 200, 400, 70])
    pantalla.blit(fuente.render(f'{ganador} ganó la partida!', True, 'white'), (210, 210))  # ganador 
    pantalla.blit(fuente.render(f'¡Presiona ENTER para reiniciar!', True, 'white'), (210, 240))  # presiona ENTER para reiniciar


# bucle principal del juego
opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  
opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  
empieza = True  
while empieza:  
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
        Valido(movimientosValidos)  
    # manejo de eventos
    for evento in pygame.event.get():  # Recorre todos los eventos del juego
        if evento.type == pygame.QUIT:  # Si el usuario cierra la ventana
            empieza = False  # Se detiene el bucle principal del juego

        # Si se hace clic izquierdo (botón 1) y el juego no ha terminado
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not gameOver:

            # Convierte la posición del clic en coordenadas del tablero (8x8 casillas de 100 píxeles)
            coordenadaX = evento.pos[0] // 100  
            coordenadaY = evento.pos[1] // 100  
            clickCoordenadas = (coordenadaX, coordenadaY)  # Coordenadas en forma de tupla (x, y)

            # ----- TURNO DE LAS BLANCAS -----
            if pasoTurno <= 1:

                # Si el jugador hace clic en (8,8) o (9,8), se considera rendición
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'negras'  # Ganan las piezas negras

                # Si se hace clic en una pieza blanca
                if clickCoordenadas in zonaBlancas:
                    seleccion = zonaBlancas.index(clickCoordenadas)  # Se guarda qué pieza fue seleccionada
                    if pasoTurno == 0:
                        pasoTurno = 1  # Se pasa al paso siguiente para elegir movimiento

                # Si se hace clic en un movimiento válido y hay una pieza previamente seleccionada
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaBlancas[seleccion] = clickCoordenadas  # Se mueve la pieza blanca seleccionada a la nueva posición

                    # Si en la casilla destino hay una pieza negra, se captura
                    if clickCoordenadas in zonaNegras:
                        piezaNegra = zonaNegras.index(clickCoordenadas)
                        comidasBlancas.append(piezasNegras[piezaNegra])  # Se guarda la pieza capturada
                        if piezasNegras[piezaNegra] == 'rey':
                            ganador = 'blancas'  # Si la pieza capturada es el rey, ganan las blancas
                        piezasNegras.pop(piezaNegra)  # Elimina la pieza capturada
                        zonaNegras.pop(piezaNegra)

                    # Se actualizan los posibles movimientos de ambos bandos
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  

                    # Se pasa el turno a las negras
                    pasoTurno = 2
                    seleccion = 100  # Se reinicia la selección
                    movimientosValidos = []  # Se limpian los movimientos válidos

            # ----- TURNO DE LAS NEGRAS -----
            if pasoTurno > 1:

                # Rendición del jugador negro
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'blancas'  # Ganan las blancas

                # Selección de pieza negra
                if clickCoordenadas in zonaNegras:
                    seleccion = zonaNegras.index(clickCoordenadas)
                    if pasoTurno == 2:
                        pasoTurno = 3  # Se pasa al siguiente paso para mover

                # Movimiento válido para pieza negra
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaNegras[seleccion] = clickCoordenadas  # Se mueve la pieza negra seleccionada

                    # Captura de pieza blanca
                    if clickCoordenadas in zonaBlancas:
                        piezaBlanca = zonaBlancas.index(clickCoordenadas)
                        comidasNegras.append(piezasBlancas[piezaBlanca])
                        if piezasBlancas[piezaBlanca] == 'rey':
                            ganador = 'negras'  # Si se captura el rey, ganan las negras
                        piezasBlancas.pop(piezaBlanca)
                        zonaBlancas.pop(piezaBlanca)

                    # Se actualizan los movimientos posibles
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  

                    # Se regresa el turno a las blancas
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
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  

        if ganador != '':
            gameOver = True
            dibujaFinDeJuego()  

    pygame.display.flip()
pygame.quit()




