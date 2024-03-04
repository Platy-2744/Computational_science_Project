import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pygame

class Graph:
    def __init__(self):
        self.__n_card = [3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52] #ชุดดไพ่ทั้งหมด
    
    #ฟังก์ชั่นเพิ่มข้อมูล
    def addData(self,correct,select):
        #กำหนดค่าตามทฤษฎี
        self.__solutaion = np.array(correct)
        self.__answer = np.array(select)
        self.__size_sol = np.size(self.__solutaion)
        self.__size_ans = np.size(self.__answer)
        self.__correct = self.__answer==self.__solutaion[:self.__size_ans] if self.__size_ans < self.__size_sol else self.__answer==np.concatenate((self.__solutaion,np.zeros(self.__size_ans-self.__size_sol)))
        self.__correct = np.size(self.__correct[self.__correct == True])
        
        #หากเล่นเกมครั้งแรกให้สร้างไฟล์ csv มาเก็บข้อมูลผู้เล่น
        try:
            self.__c_data = pd.read_csv('C_data.csv')
            self.__r_data = pd.read_csv('R_data.csv')

            #คำนวณค่าตามทฤษฎี
            self.__new_c_data = {i:j for i,j in list(zip(self.__n_card,list(np.zeros(20))))}
            self.__new_c_data[self.__size_sol] = self.__correct
            self.__new_r_data = {i:j for i,j in list(zip(self.__n_card,list(np.zeros(20))))}
            self.__new_r_data[self.__size_sol] = 3*np.pi*self.__size_ans/2
            
            #เพิ่มค่าใหม่ลงไฟล์
            self.__c_data.loc[len(self.__c_data.index)] = self.__new_c_data.values()
            self.__r_data.loc[len(self.__r_data.index)] = self.__new_r_data.values()

            self.__c_data.to_csv('C_data.csv',index=False)
            self.__r_data.to_csv('R_data.csv',index=False)

        #กรณีเคยเล่นแล้ว ให้เปิดไฟล์แล้วบันทึกค่าใหม่ลงไป
        except:
            self.__c_data = pd.DataFrame(columns=self.__n_card)
            self.__r_data = pd.DataFrame(columns=self.__n_card)
            self.__new_c_data = {i:j for i,j in list(zip(self.__n_card,list(np.zeros(20))))}
            self.__new_c_data[self.__size_sol] = self.__correct
            self.__new_r_data = {i:j for i,j in list(zip(self.__n_card,list(np.zeros(20))))}
            self.__new_r_data[self.__size_sol] = 3*np.pi*self.__size_ans/2
            
            self.__c_data.loc[len(self.__c_data.index)] = self.__new_c_data.values()
            self.__r_data.loc[len(self.__r_data.index)] = self.__new_r_data.values()

            self.__c_data.to_csv('C_data.csv',index=False)
            self.__r_data.to_csv('R_data.csv',index=False)

    def save_graph(self):
        #ทำการคำนวณค่า x ตามทฤษฎี สำหรับนำมา plot กราฟ
        self.__c_data = pd.read_csv('C_data.csv')
        self.__r_data = pd.read_csv('R_data.csv')
        self.__avg_c = [np.sum(i)/np.size(i[i!=0]) for i in self.__c_data.to_numpy().transpose()]
        self.__avg_r = [np.sum(i)/np.size(i[i!=0]) for i in self.__r_data.to_numpy().transpose()]
        self.__x_value = [np.sqrt(i/j) for i,j in list(zip(self.__avg_c,self.__avg_r))]

        #ทำการ plot กราฟ
        plt.plot(self.__n_card,self.__x_value,'ro')
        plt.axhline(y = 0.46,color = 'b', linestyle = '-') 
        plt.title('The value of memory invariant vs Amount of cards')
        plt.xlabel('L')
        plt.ylabel('X')
        plt.xticks(self.__n_card)
        plt.legend(['3 sec'])

        #บันทึกกราฟเป็นไฟล์ png
        plt.savefig('graph.png')
        
        #แสดงกราฟบน screen
    def show_graph(self,screen):
        self.__graph = pygame.image.load('graph.png')
        self.__graph_rect = self.__graph.get_rect(center=screen.get_rect().center)
        screen.blit(self.__graph,self.__graph_rect)
        
