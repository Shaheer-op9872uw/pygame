import pygame 
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 53

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("big. jpg"), 
                    SCREEN_WIDTH, SCREEN_HEIGHT)
font = pygame.font,SysFont("Times new Roman", FONT_SIZE)

class Spites(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue'))        
        pygamedraw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max()