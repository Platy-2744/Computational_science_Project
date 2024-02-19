
import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Computational Science Project')
        self.screen_size = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode()
        self.screen.fill([0,100,0])
        self.font = pygame.font.SysFont(None,45)

    def quit_buttonI(self):
        self.buttonI = pygame.draw.rect(self.screen,(0,0,0),(self.screen_size[0]/10,self.screen_size[1]/10*9 ,80,50))
        self.screen.blit(self.font.render("Quit",True,(255,255,255)),(self.screen_size[0]/10,self.screen_size[1]/10*9 ))
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttonI.topleft[0] <= pygame.mouse.get_pos()[0] <= self.buttonI.topright[0] and self.buttonI.topleft[1] <= pygame.mouse.get_pos()[1] <= self.buttonI.bottomleft[1]:
                pygame.quit()

    def stateI(self):
        self.running = True
        self.logo = pygame.image.load("images\pngegg_1.png")
        self.logo = pygame.transform.scale(self.logo,(100,100))
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (self.screen_size[0]/2,self.screen_size[1]/2-100)      
        pygame.draw.rect(self.screen,(0,0,0),(self.screen_size[0]/2-40,self.screen_size[1]/2+50 ,80,50))

        while self.running:
            for self.event in pygame.event.get():
                self.quit_buttonI()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen_size[0]/2-40 <= pygame.mouse.get_pos()[0] <= self.screen_size[0]/2+40 and self.screen_size[1]/2+50 <= pygame.mouse.get_pos()[1] <= self.screen_size[1]/2+100:
                        self.running = False

            self.screen.blit(self.logo,self.logo_rect)
            self.screen.blit(self.font.render("Start",True,(255,255,255)),(self.screen_size[0]/2-40,self.screen_size[1]/2+50))
            pygame.display.update()
            self.clock.tick(60)

    def stateII(self):
        self.running = True
        self.text = ''
        self.ncard_time = []
        while self.running:
            for self.event in pygame.event.get():
                self.screen.fill([0,100,0])
                self.quit_buttonI()
                pygame.draw.rect(self.screen,(0,0,0),(self.screen_size[0]/2-400,self.screen_size[1]/2-50,800,100))
                self.enter_button = pygame.draw.rect(self.screen,(0,0,0),(self.screen_size[0]/2-100,self.screen_size[1]/2+150,200,50))
                
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.enter_button.left <= pygame.mouse.get_pos()[0] <= self.enter_button.right and self.enter_button.top <= pygame.mouse.get_pos()[1] <= self.enter_button.bottom:
                        self.ncard_time.append(int(self.text))
                        self.text = ''


                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += self.event.unicode

                    if self.event.key == pygame.K_KP_ENTER:
                        self.ncard_time.append(int(self.text))
                        self.text = ''
                

            self.screen.blit(self.font.render("Enter",True,(255,255,255)),(self.screen_size[0]/2-100,self.screen_size[1]/2+150))
            self.screen.blit(self.font.render(self.text,True,(255,255,255)),(self.screen_size[0]/2-400,self.screen_size[1]/2-50))
            pygame.display.update()
            self.clock.tick(60)


a = Screen()
a.stateI()
a.stateII()

    