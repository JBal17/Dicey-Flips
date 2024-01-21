import random
import pygame
import time

pygame.init()

#define suits and values
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = range(2,15)

#create Deck class
class Deck():
    def __init__(self):
        self.deck = [] #empty list to be populated by deck.build
        self.build_deck() #build deck when creating class
        self.shuffle() # shuffle deck

    def build_deck(self):    
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = pygame.transform.scale(pygame.image.load(f'images\cards\{self.value}_of_{self.suit}.png').convert(), (100, 145.2)) #tuple is card size
        self.card_back = pygame.transform.scale(pygame.image.load(f'images\cards\card_back.png').convert(), (100, 145.2))
        self.discard = False
        self.face_up = True
    
    def show(self, position, surface, scale):
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.clicked = False

        pos = pygame.mouse.get_pos() #mouse position

        #check if card is clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                print('Card Clicked')
                time.sleep(0.2)
                self.face_up = not self.face_up #swap between face up and face down when clicked
            if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
        
        #draw card on screen
        if self.face_up == True:
            surface.blit(self.image, (position)) #draw card face up
        else:
            surface.blit(self.card_back, (position)) #draw card face down


class Player():
    def __init__(self):
        self.hand = []

def main():
    deck = Deck() #create a deck of cards


    player1 = Player()


if __name__ == "__main__":
    main()