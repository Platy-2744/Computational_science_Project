import pygame

class Process:
    def __init__(self) -> None:
        pass

class Process_I:
    def __init__(self) -> None:
        pygame.init()
    
    def inputN(self):
        if self.event.type == pygame.KEYDOWN:
            if pygame.Key == pygame.K_BACKSPACE:
                n = n[:-1]
            else:
                n += self.event.unicode
        return n

    def inputTime(self):
        if self.event.type == pygame.KEYDOWN:
            if pygame.Key == pygame.K_BACKSPACE:
                t = t[:-1]
            else:
                t += self.event.unicode
        return t