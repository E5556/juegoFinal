#capitulo 5 gestion de balas

# Autores:
#Karen
#Jose
#Jairo
#Edward

# Fecha: 2024/abril/15
# Versión de Python:
# Versión de Pygame:









import pygame
import Constantes
from Personaje import Personaje       # Importar la clase Personaje del archivo Personaje.py
from weapon import Weapon     # Importar la clase Weapon del archivo Weapon.py

pygame.init()   # Inicializar pygame
ventana  = pygame.display.set_mode((Constantes.ANCHO_VENTANA, Constantes.ALTO_VENTANA)) # Crear la ventana

pygame.display.set_caption("JuegoFinal") # Titulo de la ventana

def escalar_img(image, scale): # Funcion para escalar una imagen
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen


# importar imagenes

# personaje
animaciones =[]
for i in range(1, 9):
    img = pygame.image.load(f"assets//images//characters//player//TheGuy//RunAnimation48x48//{i}RunAnimation.png").convert_alpha()             # Cargar la imagen del jugador
    img = escalar_img(img, Constantes.SCALA_PERSONAJE) # Escalar la imagen del jugador
    animaciones.append(img)

# arma
imagen_pistola = pygame.image.load(f"assets//images//weapons//WeaponsB.png").convert_alpha() # Cargar la imagen del arma
imagen_pistola = escalar_img(imagen_pistola, Constantes.SCALA_ARMA) # Escalar la imagen del arma


# crear un jugador de la clase Personaje
jugador = Personaje(50, 50, animaciones)  # Crear un objeto de la clase Personaje


# crear un arma de la clase Weapon
pistola = Weapon(imagen_pistola)  # Crear un objeto de la clase Weapon


# definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False



#controlar la velocidad del juego
reloj = pygame.time.Clock()


run = True  # Variable para el bucle principal
while run == True:  # Bucle principal
    #que vaya a 60 cuadros por segundo
    reloj.tick(Constantes.FPS)
    ventana.fill(Constantes.COLOR_BG) # Pintar el fondo


    # calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = Constantes.VELOCIDAD


    if mover_izquierda == True:
        delta_x = -Constantes.VELOCIDAD



    if mover_arriba == True:
        delta_y = -Constantes.VELOCIDAD


    if mover_abajo == True:
        delta_y = Constantes.VELOCIDAD

    # mover el jugador
    jugador.movimiento(delta_x, delta_y)

    # Actualizar la animacion del jugador
    jugador.update()

    # Actualizar el estado del arma
    pistola.update(jugador)

    # dibujar al jugador
    jugador.dibujar(ventana) # Dibujar el jugador


    # dibujar al arma
    pistola.dibujar(ventana) # Dibujar el arma


    for event in pygame.event.get():    # Recorrer los eventos
        if event.type == pygame.QUIT:   # Si el evento es cerrar la ventana
            run = False

        if event.type == pygame.KEYDOWN: # Si se presiona una tecla

            if event.key == pygame.K_a:   # Si la tecla es la a
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        #para cuando se suelte la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False







    pygame.display.update()           # Actualizar la pantalla

pygame.quit() # Salir de pygame
pass
