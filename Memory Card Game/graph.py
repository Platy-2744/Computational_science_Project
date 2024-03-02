import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pygame

class Graph:
    def __init__(self):
        pass
    
    def addData(self,correct,select):
        self.solutaion = np.array(correct)
        self.answer = np.array(select)
        self.size_sol = np.size(self.solutaion)
        self.size_ans = np.size(self.answer)
        self.correct = np.size([i for i in self.answer if i in self.solutaion])
        try:
            self.c_data = pd.read_csv('C_data.csv')
            self.r_data = pd.read_csv('R_data.csv')
            self.new_c_data = {i:j for i,j in list(zip([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52],list(np.zeros(20))))}
            self.new_c_data[self.size_sol] = (1+self.correct/self.size_sol)/2
            self.new_r_data = {i:j for i,j in list(zip([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52],list(np.zeros(20))))}
            self.new_r_data[self.size_sol] = np.sqrt(3*np.pi*self.size_ans/2)
            
            self.c_data.loc[len(self.c_data.index)] = self.new_c_data.values()
            self.r_data.loc[len(self.r_data.index)] = self.new_r_data.values()

            self.c_data.to_csv('C_data.csv',index=False)
            self.r_data.to_csv('R_data.csv',index=False)

        except:
            self.c_data = pd.DataFrame(columns=[3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52])
            self.r_data = pd.DataFrame(columns=[3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52])
            self.new_c_data = {i:j for i,j in list(zip([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52],list(np.zeros(20))))}
            self.new_c_data[self.size_sol] = (1+self.correct/self.size_sol)/2
            self.new_r_data = {i:j for i,j in list(zip([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52],list(np.zeros(20))))}
            self.new_r_data[self.size_sol] = np.sqrt(3*np.pi*self.size_ans/2)
            
            self.c_data.loc[len(self.c_data.index)] = self.new_c_data.values()
            self.r_data.loc[len(self.r_data.index)] = self.new_r_data.values()

            self.c_data.to_csv('C_data.csv',index=False)
            self.r_data.to_csv('R_data.csv',index=False)

    def save_graph(self):
        self.c_data = pd.read_csv('C_data.csv')
        self.r_data = pd.read_csv('R_data.csv')
        self.avg_c = [np.sum(i)/np.size(i) for i in self.c_data.to_numpy().transpose()]
        self.avg_r = [np.sum(i)/np.size(i) for i in self.r_data.to_numpy().transpose()]
        self.x_value = [np.sqrt(k*(2*i-1))/j for i,j,k in list(zip(self.avg_c,self.avg_r,[3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52]))]

        plt.plot([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52],self.x_value,'bo')
        plt.title('The value of memory invariant vs Amount of cards')
        plt.xlabel('L')
        plt.ylabel('X')
        plt.xticks([3,5,8,10,13,16,18,21,23,26,29,31,34,36,39,42,44,47,49,52])
        plt.ylim(0,0.5)
        plt.legend(['3 sec'])
        plt.savefig('graph.png')
        
    def show_graph(self,screen):
        self.graph = pygame.image.load('graph.png')
        self.graph_rect = self.graph.get_rect(center=screen.get_rect().center)
        screen.blit(self.graph,self.graph_rect)
        
