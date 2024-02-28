import pygame, sys
from button import Button
from card import Rand_card,Select_card

pygame.init()
screen_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('beta02')
screen.fill([0,100,0])
logo = pygame.image.load('images\pngegg_1.png')
logo = pygame.transform.scale(logo,(180,162))
logo_rect = logo.get_rect(center=(screen.get_rect().center))
clock = pygame.time.Clock()


def get_font(size):
    return pygame.font.SysFont(None,size)

def quit_button(pos):
    quit_text = get_font(50).render('Quit',True,'black','white')
    screen.blit(quit_text,(0,screen.get_rect().bottom-50))
    if pos[0]<=200 and pos[0]>=0 and pos[1]<=screen.get_rect().bottom and pos[1]>=screen.get_rect().bottom-50:
        pygame.quit()
        sys.exit()

def Quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def check(correct,select):
    screen.fill([0,100,0])
    timer = 3
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while True:
        if correct == select:
            for event in pygame.event.get():
                Quit(event)
                if event.type == pygame.USEREVENT:
                    timer -= 1
                correct_text = get_font(100).render('CORRECT',True,'black','white')
                correct_rect = correct_text.get_rect(center=screen.get_rect().center)
                screen.blit(correct_text,correct_rect)
                if timer == 0:
                    remember_card()
        else:
            for event in pygame.event.get():
                Quit(event)
                if event.type == pygame.USEREVENT:
                    timer -= 1
                correct_text = get_font(100).render('WRONG',True,'black','white')
                correct_rect = correct_text.get_rect(center=screen.get_rect().center)
                screen.blit(correct_text,correct_rect)
                if timer == 0:
                    remember_card()

        pygame.display.update()
    

def select_card(list_card):
    screen.fill([0,100,0])
    sel_c = Select_card(screen,screen_size[0],screen_size[1],list_card)
    while True:
        mouse_pos = pygame.mouse.get_pos()
        quit_text = get_font(50).render('Quit',True,'black','white')
        screen.blit(quit_text,(0,screen.get_rect().bottom-50))
        select_button = Button(screen,(100,screen.get_rect().centery+300),'Select',get_font(50),'black')
        select_button.update()

        for event in pygame.event.get():
            Quit(event)
            sel_c.show_card()

            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_button(mouse_pos)
                sel_c.select_card(mouse_pos)
                correct_card, select_card = sel_c.get_correct_and_answer()

                if select_button.check_of_interect(mouse_pos):
                    check(correct_card,select_card)
           
        pygame.display.update()

def remember_card():
    screen.fill([0,100,0])
    timer = 3
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    list_button = [3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52]
    switch = False

    while True:
        mouse_pos = pygame.mouse.get_pos()
        rand_n_card = {i:Button(screen,(100,screen.get_rect().centery+300-list_button.index(i)*35),f'{i} cards',get_font(50),'black') for i in list_button}
        for button in rand_n_card.values():
            button.update()
        quit_text = get_font(50).render('Quit',True,'black','white')
        screen.blit(quit_text,(0,screen.get_rect().bottom-50))
        
        for event in pygame.event.get():
            Quit(event)
            
            if event.type == pygame.USEREVENT:
                timer -= 1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                quit_button(mouse_pos)
                for n,button in rand_n_card.items():
                    if button.check_of_interect(mouse_pos):
                        timer = 3
                        cards = Rand_card(n,screen,screen_size[0],screen_size[1])
                        cards.update()
                        switch = True

                

            if timer == 0 and switch:
                select_card(cards.get_list_of_rand_card())

        pygame.display.update()


def play():
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        quit_text = get_font(50).render('Quit',True,'black','white')
        screen.blit(quit_text,(0,screen.get_rect().bottom-50))
        screen.blit(logo,logo_rect)
        
        play_button = Button(screen,(screen.get_rect().centerx,screen.get_rect().centery+100),'Play',get_font(50),'black')
        play_button.update()
        

        for event in pygame.event.get():
            Quit(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_button(mouse_pos)
                if play_button.check_of_interect(mouse_pos):
                    remember_card()
                

        pygame.display.update()


play()