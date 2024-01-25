import random
import pygame

pygame.init()

class Player:
    def __init__(self, initial_location):
        self.initial_location = initial_location # (x, y)
        self.initial_x = initial_location[0]
        self.inital_y = initial_location[1]
        self.die_location = (self.initial_x, self.inital_y - 25)
        self.no_of_cards = 0
        self.hand = []
        self.card_locations = []
        self.die_face = None






    

