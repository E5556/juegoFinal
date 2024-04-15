import pygame
import Constantes
import math

class Weapon():
    def __init__(self, imagen):      # Constructor de la clase
        self.imagen_original = imagen
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):                     # Funcion para actualizar la animacion del personaje
        self.forma.center = personaje.forma.center                # Actualizar la posicion del arma  se coloca al centro del personaje
        if personaje.flip == False:                          # Verificar si el personaje esta mirando a la izquierda
            self.forma.x = self.forma.x + personaje.forma.width / 2
            self.rotar_arma(True)
        if personaje.flip == True:                           # Verificar si el personaje esta mirando a la derecha
            self.forma.x = self.forma.x - personaje.forma.width / 2
            self.rotar_arma(False)

        # mover el arma con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        print (self.angulo)  # Imprimir el angulo de arma en la consola


    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):    # Funcion para dibujar al personaje
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz, Constantes.COLOR_ARMA, self.forma, width=1)



