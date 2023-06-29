import pygame
from gui import GUI

pygame.init()


class APP:
    def __init__(self):
        self.data = None
        self.screen = pygame.display.set_mode((800, 500))
        self.gui = GUI(self.screen)

    def check_for_inputs(self):
        self.data = input()
        try:
            self.data = int(self.data)
        except:
            pass

    def loop(self):
        while True:
            pass
