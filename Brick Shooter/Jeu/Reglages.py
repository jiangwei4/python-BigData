import pygame

class Reglages:
    def __init__(self):
        self.fireKey = pygame.K_a

    def changeKey(self, key):
        key = pygame.event.get()