import pygame
from gui import GUI

pygame.init()


class APP:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 500))
        self.gui = GUI(self.screen)

    def check_for_inputs(self):
        data = input()
        try:
            pass
        except:
            pass
    def loop(self):
        while True:
            pass
