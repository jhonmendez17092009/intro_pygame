# importmos la librerio pygame

import pygame
import random

rojo = random.randint(0, 255) 
azul = random.randint(0, 255) 
verde = random.randint(0, 255) 



# inisializamos los modulos de pygame

pygame.init()

# establecer titulo a la ventana 

pygame.display.set_caption("surface")

# establecemos las dimenciones de la ventana

ventana = pygame.display.set_mode((400,400))

# definicion del color
color_aleatorio = (rojo, verde, azul)

# crear una superficies

color_aleatorio_superficie = pygame.Surface((200,200))

# rellenar la superficie de azul


color_aleatorio_superficie.fill(azul)

# inserto o muevo la superficie de la ventana

ventana.blit(color_aleatorio_superficie, (100, 100))

# actualiza la ventana

pygame.display.flip()

# bucle 

while True: 
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break