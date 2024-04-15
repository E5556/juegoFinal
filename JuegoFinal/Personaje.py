import pygame
import Constantes

class Personaje():
    def __init__(self, x, y, animaciones):      # Constructor de la clase
        self.flip = False       # Variable para saber si el personaje esta mirando a la izquierda o derecha
        self.animaciones = animaciones
        # imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        # aqui se almacena la hora actual en milisegundos desde que se inicio pygame
        self.update_time = pygame.time.get_ticks()  # Tiempo de actualizacion de la animacion
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()  # Crear un rectangulo alrededor del personaje
        self.forma.center = (x, y)

    def movimiento(self, delta_x, delta_y): # Funcion para mover al personaje
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False


        self.forma.x = self.forma.x + delta_x # Mover al personaje en el eje x
        self.forma.y = self.forma.y + delta_y  # Mover al personaje en el eje y

    def update(self):     # Funcion para actualizar la animacion del personaje
        cooldown_animacion= 100     # tiempo que se mantien animacionantes de cambiar de frame
        self.image = self.animaciones[self.frame_index]  # Actualizar la imagen del personaje
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:    # Verificar si es tiempo de cambiar de frame
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0




    def dibujar(self, interfaz):    # Funcion para dibujar al personaje
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)   # Voltear la imagen si es necesario
        interfaz.blit(imagen_flip, self.forma)  # Dibujar al personaje en la pantalla
        #pygame.draw.rect(interfaz,  Constantes.COLOR_PERSONAJE,self.forma, width=1)    # Dibujar un rectangulo alrededor del personaje



