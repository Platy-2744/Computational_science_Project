import pygame

pygame.init()
pygame.display.set_caption('Computational Science Project')
screen = pygame.display.set_mode((800,600))
ranning = True
screen.fill([0,100,0])
pygame.display.update()
while ranning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
