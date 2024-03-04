import math
import random
import pygame

#select card class สำหรับทำให้งานในการเรียกใช้ซ้ำ
class Select_card:
    def __init__(self,screen,screen_size_x,screen_size_y,rand_card):
        self.__screen = screen
        self.__screen_size_x, self.__screen_size_y = screen_size_x, screen_size_y
        self.__first_pos = [self.__screen_size_x//8,self.__screen_size_y//10]   #จุดเริ่มของไพ่ที่แสดง
        self.__list_card = {i:pygame.transform.scale(pygame.image.load(f'images\card{i}.png'),(84,126)) for i in range(1,53)} #โหลดรูปไพ่ทั้งหมด
        self.__correct_card = rand_card #เก็บผลเฉลยที่รับมา ไว้สำหรับส่งต่อไปตรวจสอบที่ screen.py
        self.__answer = [] #ไว้เก็บคำตอบของผู้เล่น

    #ลูปแสดงไพ่ทั้งหมด
    def show_card(self):
        for card,image in self.__list_card.items():
            self.__screen.blit(image,(self.__first_pos[0]+98*(card-1) if (card-1)<13 else self.__first_pos[0]+98*((card-1)%13),self.__first_pos[1]+147*math.floor((card-1)/13)))

    #ฟังก์ชั่นเลือกไพ่
    def select_card(self,mouse_pos):
        self.__all_pos = {card:[self.__first_pos[0]+98*(card-1) if (card-1)<13 else self.__first_pos[0]+98*((card-1)%13),self.__first_pos[1]+147*math.floor((card-1)/13)] for card in self.__list_card.keys()} #ตำแหน่งของไพ่ที่แสดงทั้งหมด

        for card,pos in self.__all_pos.items():
            #ตรวจสอบว่าได้กดไพ่หรือไม่
            if pos[0]+84 >= mouse_pos[0] >= pos[0] and pos[1]+126 >= mouse_pos[1] >= pos[1]:
                if card in self.__answer:
                    pygame.draw.rect(self.__screen,[0,100,0],(pos[0]-6,pos[1]-6,96,138),5) #ถ้าเลือกไพ่นั้นในแล้ว ให้วาดกรอบสีเขียน แล้วลบออกจากรายการคำตอบ
                    self.__answer.remove(card)
                else:
                    pygame.draw.rect(self.__screen,[0,255,255],(pos[0]-6,pos[1]-6,96,138),5) #ถ้ายังไม่ได้เลือกไพ่นั่น ให้วาดกรอบสีฟ้า แล้วเพิ่มเข้าในรายการคำตอบ
                    self.__answer.append(card)
        
    def get_correct_and_answer(self):
        #ส่งไพ้ที่ถูกต้องกับไพ่ที่เลือกไปตรวจสอบที่ screen.py
        return [self.__correct_card,self.__answer]

#rand card class สำหรับทำให้งานในการเรียกใช้ซ้ำ
class Rand_card:
    def __init__(self,n,screen,screen_size_x,screen_size_y):
        self.__screen = screen
        self.__screen_size_x, self.__screen_size_y = screen_size_x, screen_size_y
        self.__n = n
        self.__list_card = {i:pygame.transform.scale(pygame.image.load(f'images\card{i}.png'),(84,126)) for i in range(1,53)} ##โหลดรูปไพ่ทั้งหมด
        self.__first_pos = [self.__screen_size_x//8,self.__screen_size_y//10]
        self.__rand_card = {i[0]:i[1] for i in random.sample(self.__list_card.items(),self.__n)} #ทำการสุ่มไพ่แบบไม่มีการซ้ำตามชุดไพ่ที่รับเข้ามา

    #แสดงไพ่ที่สุ่ม
    def update(self):
        j = 0
        for image in self.__rand_card.values():
            self.__screen.blit(image,(self.__first_pos[0]+98*j if j<13 else self.__first_pos[0]+98*(j%13),self.__first_pos[1]+147*math.floor(j/13)))
            j+=1

    #ส่งไพ่ที่สุ่มแล้ว
    def get_list_of_rand_card(self):
        return [i for i in self.__rand_card.keys()]

    