import pygame

# Inicializar Pygame
pygame.init()

# Definir constantes
ANCHO, ALTO = 900, 900
FILAS, COLUMNAS = 8, 8
TAMANO_CUADRO = ANCHO // COLUMNAS
ALTURA_INSTRUCCIONES = 100  # Espacio inferior para mostrar instrucciones
ANCHO_PIEZAS_CAPTURADAS = 200  # Espacio derecho para piezas capturadas

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
AZUL = (100, 100, 255)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO + ANCHO_PIEZAS_CAPTURADAS, ALTO + ALTURA_INSTRUCCIONES))
pygame.display.set_caption("Ajedrez")

# Diccionario para cargar las imágenes de las piezas
def cargar_imagenes():
    piezas = {}
    colores = ["blanca", "negro"]
    tipos = ["rey", "reina", "torre", "alfil", "caballo", "peon"]
    for color in colores:
        for tipo in tipos:
            nombre_archivo = f"imagenes/{color}_{tipo}.png"
            try:
                piezas[f"{color}_{tipo}"] = pygame.image.load(nombre_archivo)
            except pygame.error:
                print(f"Error: No se pudo cargar {nombre_archivo}")
    return piezas

imagenes_piezas = cargar_imagenes()

# Función para dibujar el tablero
def dibujar_tablero():
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            color = BLANCO if (fila + col) % 2 == 0 else NEGRO
            pygame.draw.rect(ventana, color, (col * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))

# Dibujar el área de instrucciones
def dibujar_instrucciones():
    pygame.draw.rect(ventana, GRIS, (0, ALTO, ANCHO, ALTURA_INSTRUCCIONES))
    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render("Turno: Blancas", True, NEGRO)
    ventana.blit(texto, (20, ALTO + 30))

# Dibujar el área de piezas capturadas
def dibujar_piezas_capturadas():
    pygame.draw.rect(ventana, AZUL, (ANCHO, 0, ANCHO_PIEZAS_CAPTURADAS, ALTO))
    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render("Piezas Capturadas", True, BLANCO)
    ventana.blit(texto, (ANCHO + 20, 20))

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    dibujar_tablero()
    dibujar_instrucciones()
    dibujar_piezas_capturadas()
    pygame.display.flip()

pygame.quit()









pygame.display.update()