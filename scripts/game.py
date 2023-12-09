import pygame
import os

class Game:
    def __init__(self) -> None:
        self.background = pygame.image.load(os.path.join('assets','images','background.png'))

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (0,0))