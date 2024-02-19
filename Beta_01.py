import pygame

pygame.init()
pygame.display.set_caption('beta')
screenSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode()

stateI = True
stateII = False

ranning = True
while stateI:
    for event in pygame.event.get():
        screen.fill([0,100,0])
        pygame.draw.rect(screen,(0,0,0),(screenSize[0]/10,screenSize[1]/10*9 ,80,50),5)
        
        if event.type == pygame.QUIT:
            ranning = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screenSize[0]/2-40 <= pygame.mouse.get_pos()[0] <= screenSize[0]/2+40 and screenSize[1]/2+50 <= pygame.mouse.get_pos()[1] <= screenSize[1]/2+100:
                stateI = False
                stateII = True

        logo = pygame.image.load("images\pngegg_1.png")
        logo = pygame.transform.scale(logo,(100,100))
        screen.blit(logo,(screenSize[0]/2-50,screenSize[1]/2-200))
        pygame.draw.rect(screen,(0,0,0),(screenSize[0]/2-40,screenSize[1]/2+50 ,80,50),5)

    pygame.display.update()

while stateII:
    for event in pygame.event.get():
        screen.fill([0,100,0])
        pygame.draw.rect(screen,(0,0,0),(screenSize[0]/10,screenSize[1]/10*9 ,80,50),5)

        if event.type == pygame.QUIT:
            ranning = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screenSize[0]/10 <= pygame.mouse.get_pos()[0] <= screenSize[0]/10+80 and screenSize[1]/10*9 <= pygame.mouse.get_pos()[1] <= screenSize[1]/10*9+50:
                pygame.quit()

        pygame.draw.rect(screen,(0,0,255),(screenSize[0]/2-40,screenSize[1]/2+50 ,80,50),5)
        
    pygame.display.update()