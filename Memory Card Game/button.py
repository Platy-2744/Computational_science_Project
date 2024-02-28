
class Button:
    def __init__(self,screen,pos,text,font,color='black'):
        self.screen = screen
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.font = font
        self.text = self.font.render(text,True,color,'white')
        self.text_rect = self.text.get_rect(center=(self.pos_x,self.pos_y))

        self.quit_button_size = (800,400)


    def update(self):
        self.screen.blit(self.text,self.text_rect)
        
    def check_of_interect(self, pos):
        if pos[0]<=self.text_rect.right and pos[0]>=self.text_rect.left and pos[1]<=self.text_rect.bottom and pos[1]>=self.text_rect.top:
            return True
        else:
            return False
