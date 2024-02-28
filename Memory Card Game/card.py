import math
import random
import pygame

class Select_card:
    def __init__(self,screen,screen_size_x,screen_size_y,rand_card):
        self.screen = screen
        self.screen_size_x, self.screen_size_y = screen_size_x, screen_size_y
        self.first_pos = [self.screen_size_x//8,self.screen_size_y//10]
        self.list_card = {i:pygame.transform.scale(pygame.image.load(f'images\card{i}.png'),(84,126)) for i in range(1,53)}
        self.correct_card = rand_card
        self.answer = []

    def show_card(self):
        for card,image in self.list_card.items():
            self.screen.blit(image,(self.first_pos[0]+98*(card-1) if (card-1)<13 else self.first_pos[0]+98*((card-1)%13),self.first_pos[1]+147*math.floor((card-1)/13)))

    def select_card(self,mouse_pos):
        self.all_pos = {card:[self.first_pos[0]+98*(card-1) if (card-1)<13 else self.first_pos[0]+98*((card-1)%13),self.first_pos[1]+147*math.floor((card-1)/13)] for card in self.list_card.keys()}

        for card,pos in self.all_pos.items():
            if pos[0]+84 >= mouse_pos[0] >= pos[0] and pos[1]+126 >= mouse_pos[1] >= pos[1]:
                if card in self.answer:
                    pygame.draw.rect(self.screen,[0,100,0],(pos[0]-6,pos[1]-6,96,138),5)
                    self.answer.remove(card)
                else:
                    pygame.draw.rect(self.screen,[0,255,255],(pos[0]-6,pos[1]-6,96,138),5)
                    self.answer.append(card)
        
    def get_correct_and_answer(self):
        return [self.correct_card,self.answer]


class Rand_card:
    def __init__(self,n,screen,screen_size_x,screen_size_y):
        self.screen = screen
        self.screen_size_x, self.screen_size_y = screen_size_x, screen_size_y
        self.n = n
        self.list_card = {i:pygame.transform.scale(pygame.image.load(f'images\card{i}.png'),(84,126)) for i in range(1,53)}
        self.first_pos = [self.screen_size_x//8,self.screen_size_y//10]
        self.all_pos = {card:[self.first_pos[0]+98*(card-1) if (card-1)<13 else self.first_pos[0]+98*((card-1)%13),self.first_pos[1]+147*math.floor((card-1)/13)] for card in self.list_card.keys()}
        self.rand_card = {i[0]:i[1] for i in random.sample(self.list_card.items(),self.n)}

    def update(self):
        j = 0
        for image in self.rand_card.values():
            self.screen.blit(image,(self.first_pos[0]+98*j if j<13 else self.first_pos[0]+98*(j%13),self.first_pos[1]+147*math.floor(j/13)))
            j+=1

    def get_list_of_rand_card(self):
        return [i for i in self.rand_card.keys()]

    