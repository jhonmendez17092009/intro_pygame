import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Recolector de monedas")

BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.velocidad = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidad

class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

todos_los_sprites = pygame.sprite.Group()
monedas = pygame.sprite.Group()

personaje = Personaje()
todos_los_sprites.add(personaje)

for i in range(5):
    moneda = Moneda(100 * (i + 1), 100 * (i + 1))
    todos_los_sprites.add(moneda)
    monedas.add(moneda)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    todos_los_sprites.update()

    colisiones = pygame.sprite.spritecollide(personaje, monedas, True)

    screen.fill(BLANCO)

    todos_los_sprites.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()