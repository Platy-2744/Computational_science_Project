import pygame, sys
from button import Button

pygame.init()
screen_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('beta02')
screen.fill([0,100,0])
logo = pygame.image.load('images\pngegg_1.png')
logo = pygame.transform.scale(logo,(180,162))
logo_rect = logo.get_rect(center=(screen.get_rect().center))

def get_font(size):
    return pygame.font.SysFont(None,size)

def quit_button(pos):
    quit_text = get_font(50).render('Quit',True,'black','white')
    screen.blit(quit_text,(0,screen.get_rect().bottom-50))
    if pos[0]<=200 and pos[0]>=0 and pos[1]<=screen.get_rect().bottom and pos[1]>=screen.get_rect().bottom-50:
        pygame.quit()
        sys.exit()

def game():
    pass

def play():
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        quit_text = get_font(50).render('Quit',True,'black','white')
        screen.blit(quit_text,(0,screen.get_rect().bottom-50))
        screen.blit(logo,logo_rect)
        
        play_button = Button(screen,(screen.get_rect().centerx,screen.get_rect().centery+100),'Play',get_font(50),'black')
        play_button.update()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_button(mouse_pos)
                if play_button.check_of_interect(mouse_pos):
                    game()
                

        pygame.display.update()


play()