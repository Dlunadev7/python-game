# -*- coding: utf-8 -*-

import pygame
import random

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Creación de la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi juego")

# Clase del personaje
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super(Personaje, self).__init__()
        self.imagen = pygame.Surface((50, 50))
        self.imagen.fill(BLANCO)
        self.rect = self.imagen.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        # Movimiento del personaje con las teclas de flecha
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5

        # Limitar el movimiento del personaje dentro de la ventana
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

# Clase de los obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstaculo, self).__init__()
        self.image = pygame.Surface((30, random.randint(50, 200)))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO
        self.rect.y = random.randint(0, ALTO - self.rect.height)
        self.velocidad = random.randint(1, 5)

    def update(self):
        # Movimiento del obstáculo hacia la izquierda
        self.rect.x -= self.velocidad

        # Eliminar el obstáculo cuando sale de la pantalla
        if self.rect.right < 0:
            self.kill()

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Creación del personaje
personaje = Personaje()
# todos_los_sprites.add(personaje)

# Reloj para controlar la velocidad del jbbuego
reloj = pygame.time.Clock()

# Bucle principal del juego
juego_terminado = False
while not juego_terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    # Crear nuevos obstáculos de forma aleatoria
    if random.randint(0, 100) < 3:
        obstaculo = Obstaculo()
        obstaculos.add(obstaculo)
        todos_los_sprites.add(obstaculo)

    # Actualizar sprites
    todos_los_sprites.update()

    # Comprobar colisiones entre el personaje y los obstáculos
    if pygame.sprite.spritecollide(personaje, obstaculos, False):
        juego_terminado = True

    # Limpiar la pantalla
    ventana.fill(BLANCO)

    # Dibujar todos los sprites en la ventana
    todos_los_sprites.draw(ventana)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de fotogramas del juego
    reloj.tick(60)

# Salir del juego
pygame.quit()