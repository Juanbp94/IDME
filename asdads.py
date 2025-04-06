
import pygame

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH = 1000
HEIGHT = 900
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])  # Crea la ventana del juego
pygame.display.set_caption('1vs1 Ajedrez')  # Título de la ventana

# Fuentes para los textos
fuente = pygame.font.Font('freesansbold.ttf', 20)
fuenteMediana = pygame.font.Font('freesansbold.ttf', 40)
fuenteGrande = pygame.font.Font('freesansbold.ttf', 50)

temporizador = pygame.time.Clock()  # Temporizador para controlar FPS
fps = 60

# Inicialización de piezas y posiciones
piezasBlancas = [...]  # Lista de piezas blancas
zonaBlancas = [...]  # Posiciones iniciales de las piezas blancas
piezasNegras = [...]  # Lista de piezas negras
zonaNegras = [...]  # Posiciones iniciales de las piezas negras
comidasBlancas = []  # Lista de piezas capturadas blancas
comidasNegras = []  # Lista de piezas capturadas negras

# Inicialización de variables de juego
pasoTurno = 0  # Controla el turno
seleccion = 100  # Controla la selección de piezas
movimientosValidos = []  # Lista de movimientos válidos
contador = 0  # Contador para efectos visuales
ganador = ''  # Almacena el ganador
gameOver = False  # Estado del juego

# Función para dibujar el tablero
def tablero():
    # Dibuja el tablero de ajedrez
    for i in range(32):
        columna = i % 4  # Calcula la columna
        fila = i // 4  # Calcula la fila
        # Alterna el color de las casillas
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, 'light gray', [600 - (columna * 200), fila * 100, 100, 100])
        else:
            pygame.draw.rect(pantalla, 'light gray', [700 - (columna * 200), fila * 100, 100, 100])
    
    # Dibuja la parte inferior del tablero y el texto de estado
    pygame.draw.rect(pantalla, 'gray', [0, 800, WIDTH, 100])
    pygame.draw.rect(pantalla, 'gold', [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(pantalla, 'gold', [800, 0, 200, HEIGHT], 5)
    
    texto = ['Blancas: ¡Selecciona una pieza para mover!', 'Blancas: ¡Selecciona un destino!',
             'Negras: ¡Selecciona una pieza para mover!', 'Negras: ¡Selecciona un destino!']
    pantalla.blit(fuenteGrande.render(texto[pasoTurno], True, 'black'), (20, 820))
    
    # Dibuja las líneas del tablero
    for i in range(9):
        pygame.draw.line(pantalla, 'black', (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(pantalla, 'black', (100 * i, 0), (100 * i, 800), 2)
    pantalla.blit(fuenteMediana.render('RENDIRSE', True, 'black'), (810, 830))

# Función para colocar las piezas en el tablero
def colocaPiezas():
    # Dibuja las piezas blancas
    for i in range(len(piezasBlancas)):
        indicePiezas = listaPiezas.index(piezasBlancas[i])  # Encuentra el índice de la pieza
        if piezasBlancas[i] == 'peon':
            pantalla.blit(peonBlanca, (zonaBlancas[i][0] * 100 + 22, zonaBlancas[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesBlancas[indicePiezas], (zonaBlancas[i][0] * 100 + 10, zonaBlancas[i][1] * 100 + 10))
        
        # Resalta la pieza seleccionada
        if pasoTurno < 2 and seleccion == i:
            pygame.draw.rect(pantalla, 'red', [zonaBlancas[i][0] * 100 + 1, zonaBlancas[i][1] * 100 + 1, 100, 100], 2)

    # Dibuja las piezas negras
    for i in range(len(piezasNegras)):
        indicePiezas = listaPiezas.index(piezasNegras[i])  # Encuentra el índice de la pieza
        if piezasNegras[i] == 'peon':
            pantalla.blit(peonNegra, (zonaNegras[i][0] * 100 + 22, zonaNegras[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenesNegras[indicePiezas], (zonaNegras[i][0] * 100 + 10, zonaNegras[i][1] * 100 + 10))
        
        # Resalta la pieza seleccionada
        if pasoTurno >= 2 and seleccion == i:
            pygame.draw.rect(pantalla, 'blue', [zonaNegras[i][0] * 100 + 1, zonaNegras[i][1] * 100 + 1, 100, 100], 2)

# Función para revisar movimientos de piezas que se mueven en línea recta o diagonal
def revisaMovimientoLineal(posicion, color, direcciones):
    listaMovimientos = []  # Lista para almacenar movimientos válidos
    if color == 'blancas':
        listaEnemiga = zonaNegras  # Ubicaciones de piezas negras
        ListaAliados = zonaBlancas  # Ubicaciones de piezas blancas
    else:
        ListaAliados = zonaNegras  # Ubicaciones de piezas negras
        listaEnemiga = zonaBlancas  # Ubicaciones de piezas blancas
    
    # Itera sobre las direcciones para calcular movimientos
    for direccion in direcciones:
        comoAlfil = True  # Variable para controlar el recorrido
        cuantoAlfil = 1  # Contador para avanzar en la dirección
        x, y = direccion  # Descomponer la dirección en x e y
        
        # Mientras haya un movimiento válido en la dirección
        while comoAlfil:
            # Calcular la nueva posición
            nueva_posicion = (posicion[0] + (cuantoAlfil * x), posicion[1] + (cuantoAlfil * y))
            # Verifica si la nueva posición es válida
            if nueva_posicion not in ListaAliados and 0 <= nueva_posicion[0] <= 7 and 0 <= nueva_posicion[1] <= 7:
                listaMovimientos.append(nueva_posicion)  # Añade el movimiento a la lista
                if nueva_posicion in listaEnemiga:  # Si la posición es de una pieza enemiga
                    comoAlfil = False  # Detiene el recorrido
                cuantoAlfil += 1  # Avanza en la dirección
            else:
                comoAlfil = False  # Detiene el recorrido si no es válido
    return listaMovimientos  # Devuelve los movimientos válidos

# Funciones para revisar movimientos específicos de piezas
def revisaTorre(posicion, color):
    # Direcciones para la torre (arriba, abajo, izquierda, derecha)
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return revisaMovimientoLineal(posicion, color, direcciones)  # Llama a la función general

def revisaAlfil(posicion, color):
    # Direcciones para el alfil (diagonales)
    direcciones = [(1, -1), (-1, -1), (1, 1), (-1, 1)]
    return revisaMovimientoLineal(posicion, color, direcciones)  # Llama a la función general

def revisaReina(posicion, color):
    # Direcciones para la reina (combinación de torre y alfil)
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    return revisaMovimientoLineal(posicion, color, direcciones)  # Llama a la función general

# Función para revisar los movimientos válidos del rey
def revisaRey(posicion, color):
    listaMovimientos = []  # Lista para movimientos válidos
    if color == 'blancas':
        listaEnemiga = zonaNegras  # Ubicaciones de piezas negras
        ListaAliados = zonaBlancas  # Ubicaciones de piezas blancas
    else:
        ListaAliados = zonaNegras  # Ubicaciones de piezas negras
        listaEnemiga = zonaBlancas  # Ubicaciones de piezas blancas
    
    # Posibles movimientos del rey
    moviRey = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        objetivo = (posicion[0] + moviRey[i][0], posicion[1] + moviRey[i][1])  # Nueva posición
        # Verifica si el movimiento es válido
        if objetivo not in ListaAliados and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            listaMovimientos.append(objetivo)  # Añade el movimiento a la lista
    return listaMovimientos  # Devuelve los movimientos válidos

# Bucle principal del juego
opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')  # Opciones para piezas negras
opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')  # Opciones para piezas blancas
empieza = True  # Variable para controlar el ciclo del juego

while empieza:  # Bucle del juego
    temporizador.tick(fps)  # Controla el FPS
    if contador < 30:
        contador += 1  # Incrementa el contador
    else:
        contador = 0  # Reinicia el contador
    
    pantalla.fill('dark gray')  # Limpia la pantalla
    tablero()  # Dibuja el tablero
    colocaPiezas()  # Dibuja las piezas
    # Otras funciones de dibujo como capturadas, jaque, etc.

    # Manejo de eventos
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:  # Si se cierra la ventana
            empieza = False  # Termina el juego
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not gameOver:
            coordenadaX = evento.pos[0] // 100  # Calcula la coordenada X
            coordenadaY = evento.pos[1] // 100  # Calcula la coordenada Y
            clickCoordenadas = (coordenadaX, coordenadaY)  # Almacena las coordenadas del clic
            
            # Lógica para el turno de las piezas blancas
            if pasoTurno <= 1:
                # Comprobar si se ha hecho clic en la casilla de rendición
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'negras'  # Las negras ganan
                # Comprobar si se ha hecho clic en una pieza blanca
                if clickCoordenadas in zonaBlancas:
                    seleccion = zonaBlancas.index(clickCoordenadas)  # Selecciona la pieza
                    if pasoTurno == 0:
                        pasoTurno = 1  # Cambia a seleccionar destino
                # Comprobar si se ha hecho clic en un movimiento válido
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaBlancas[seleccion] = clickCoordenadas  # Mueve la pieza
                    # Comprueba si captura una pieza negra
                    if clickCoordenadas in zonaNegras:
                        piezaNegra = zonaNegras.index(clickCoordenadas)
                        comidasBlancas.append(piezasNegras[piezaNegra])  # Añade a las comidas
                        if piezasNegras[piezaNegra] == 'rey':
                            ganador = 'blancas'  # Las blancas ganan si capturan al rey
                        piezasNegras.pop(piezaNegra)  # Elimina la pieza negra capturada
                        zonaNegras.pop(piezaNegra)  # Elimina su ubicación
                    # Actualiza las opciones de movimientos
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')
                    pasoTurno = 2  # Cambia de turno
                    seleccion = 100  # Reinicia la selección
                    movimientosValidos = []  # Reinicia movimientos válidos
            
            # Lógica para el turno de las piezas negras
            if pasoTurno > 1:
                # Comprobar si se ha hecho clic en la casilla de rendición
                if clickCoordenadas == (8, 8) or clickCoordenadas == (9, 8):
                    ganador = 'blancas'  # Las blancas ganan
                # Comprobar si se ha hecho clic en una pieza negra
                if clickCoordenadas in zonaNegras:
                    seleccion = zonaNegras.index(clickCoordenadas)  # Selecciona la pieza
                    if pasoTurno == 2:
                        pasoTurno = 3  # Cambia a seleccionar destino
                # Comprobar si se ha hecho clic en un movimiento válido
                if clickCoordenadas in movimientosValidos and seleccion != 100:
                    zonaNegras[seleccion] = clickCoordenadas  # Mueve la pieza
                    # Comprueba si captura una pieza blanca
                    if clickCoordenadas in zonaBlancas:
                        piezaBlanca = zonaBlancas.index(clickCoordenadas)
                        comidasNegras.append(piezasBlancas[piezaBlanca])  # Añade a las comidas
                        if piezasBlancas[piezaBlanca] == 'rey':
                            ganador = 'negras'  # Las negras ganan si capturan al rey
                        piezasBlancas.pop(piezaBlanca)  # Elimina la pieza blanca capturada
                        zonaBlancas.pop(piezaBlanca)  # Elimina su ubicación
                    # Actualiza las opciones de movimientos
                    opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')
                    opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')
                    pasoTurno = 0  # Cambia de turno
                    seleccion = 100  # Reinicia la selección
                    movimientosValidos = []  # Reinicia movimientos válidos

        # Reinicia el juego si se presiona ENTER después de que el juego haya terminado
        if evento.type == pygame.KEYDOWN and gameOver:
            if evento.key == pygame.K_RETURN:
                gameOver = False  # Reinicia el estado de juego
                ganador = ''  # Reinicia el ganador
                # Reinicia las piezas y sus posiciones
                piezasBlancas = [...]
                zonaBlancas = [...]
                piezasNegras = [...]
                zonaNegras = [...]
                comidasBlancas = []  # Reinicia capturadas
                comidasNegras = []  # Reinicia capturadas
                pasoTurno = 0  # Reinicia el turno
                seleccion = 100  # Reinicia la selección
                movimientosValidos = []  # Reinicia movimientos válidos
                opcionesNegras = opcionesValidas(piezasNegras, zonaNegras, 'negras')
                opcionesBlancas = opcionesValidas(piezasBlancas, zonaBlancas, 'blancas')

    # Si hay un ganador, muestra la pantalla de fin de juego
    if ganador != '':
        gameOver = True  # Cambia el estado del juego a terminado
        dibujaFinDeJuego()  # Dibuja la pantalla de fin de juego

    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()  # Cierra Pygame