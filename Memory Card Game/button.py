
#button class สำหรับสร้างปุ่มหลายๆปุ่ม
class Button:
    #กำหนดลักษณะของปุ่ม
    def __init__(self,screen,pos,text,font,color='black'):
        self.__screen = screen
        self.__pos_x = pos[0]
        self.__pos_y = pos[1]
        self.__font = font
        self.__text = self.__font.render(text,True,color,'white')
        self.__text_rect = self.__text.get_rect(center=(self.__pos_x,self.__pos_y))

    #แสดงปุ่มบนหน้าจอ
    def update(self):
        self.__screen.blit(self.__text,self.__text_rect)

    #ตรวจสอบการกดปุ่ม 
    def check_of_interect(self, pos):
        if pos[0]<=self.__text_rect.right and pos[0]>=self.__text_rect.left and pos[1]<=self.__text_rect.bottom and pos[1]>=self.__text_rect.top:
            return True
        else:
            return False
