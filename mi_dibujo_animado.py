import pygame
import sys
import random


color_ventana = (0, 255, 238)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
p = (255, 0, 112)
j = (0, 255, 216)
y = (255, 255, 0)
m = (115, 62, 23)
n = (0, 0, 0)
o = (255, 93, 0)
per = (108, 59, 32)
w = (255, 255, 255)
cielo = (255, 255, 255)
z = 0
t = 500




pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("lineas aleatorias")

clock = pygame.time.Clock()
while 1:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        ventana.fill(cielo)

    pygame.draw.rect(ventana, r, ((305, 0), (150, 20)))  
    pygame.draw.rect(ventana, r, ((285, 20), (190, 20)))
    pygame.draw.rect(ventana, g, ((305, 40), (150, 100)), 20)
    pygame.draw.rect(ventana, b, ((200, 80), (50, 20)))  
    pygame.draw.rect(ventana, b, ((210, 100), (30, 40)))  
    pygame.draw.circle(ventana, o, (190, 215), 65)
    pygame.draw.rect(ventana, j, ((200, 140), (280, 150)))  
    pygame.draw.rect(ventana, p, ((180, 150), (20, 130)))  
    pygame.draw.rect(ventana, p, ((150, 140), (30, 150)))
    pygame.draw.circle(ventana, m, (250, 300), 45)
    pygame.draw.circle(ventana, m, (340, 300), 45)
    pygame.draw.circle(ventana, m, (430, 300), 45)
    pygame.draw.rect(ventana, n, ((270, 290), (50, 20)))  
    pygame.draw.rect(ventana, n, ((360, 290), (50, 20)))  

    # Personita
    pygame.draw.circle(ventana, per, (380, 90), 35, 0)

    # Ojos
    pygame.draw.circle(ventana, w, (365, 80), 12, 0)
    pygame.draw.circle(ventana, w, (395, 80), 12, 0)

    # Boca
    pygame.draw.circle(ventana, r, (380, 106), 9, 0)

    # pupila 
    pygame.draw.circle(ventana, m, (365, 80), 6, 0)
    pygame.draw.circle(ventana, m, (395, 80), 6, 0)



    # Cejas
    pygame.draw.line(ventana, n, (360, 60), (370, 70), 3)
    pygame.draw.line(ventana, n, (390, 70), (400, 60), 3)

    pygame.display.flip()