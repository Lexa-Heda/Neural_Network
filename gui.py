import pygame

pygame.init()


class GUI:
    def __init__(self, root):
        self.textbox = None
        self.textbox_rect = None
        self.screen = root
        self.font = pygame.font.Font(None, 36)
        self.text = None

    def update(self, text: str):
        self.text = text
        self.textbox = self.font.render(self.text, True, (255, 255, 255))
        self.textbox_rect = self.textbox.get_rect()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.textbox, self.textbox_rect)
        pygame.display.update()
