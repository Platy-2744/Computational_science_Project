import numpy as np, pandas as pd

class RandomCard:
    def __init__(self,n) -> None:
        self.__nCard = n

def setN(self,n):self.__n = n
def getN(self):return self.__n

def rand(self):
    r = np.random.choice(range(1,53),self.__n)
    rPath = ["\Computational_science_Project\images" for i in r]
