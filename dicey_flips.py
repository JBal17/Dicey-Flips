import pygame
import sys
from deck import Deck, Player
from button import Button
import random
import time

pygame.init()

bg_colour = (53, 101, 77)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT= 720

SCREEN_CENTRE_X = SCREEN_WIDTH / 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #width, heigh

screen.fill(bg_colour)

pygame.display.set_caption('Dicey Flips')

pygame.display.flip()

INITIAL_IMAGE_SIZE = (500,726)
SCALE_FACTOR = 0.2
SCALED_IMAGE_SIZE = tuple(i * SCALE_FACTOR for i in INITIAL_IMAGE_SIZE)

# image_location = [(100, 100), (220, 100)]

P1_INITIAL_IMAGE_LOCATION_X =  100
P1_IMAGE_LOCATION_Y = SCREEN_HEIGHT - (SCALED_IMAGE_SIZE[1] + 50) #100
CARD_SPACING_X = 110

P1_DIE_LOCATION = (100,400)

number_of_cards = 0

discard_image = pygame.image.load('images\\buttons\\discard.png').convert_alpha()
deal_image = pygame.image.load('images\\buttons\\deal.png').convert_alpha()
roll_image = pygame.image.load('images\\buttons\\roll.png').convert_alpha()
#card_back = pygame.image.load('images\\cards\\card_back.png').convert_alpha()

die_roll_animation_list = []
for i in range(1,6):
    die_roll_animation_list.append(pygame.image.load(f'images\dice\dice-six-faces-{i}.png').convert())
    
def die_roll_animation(location):
    for i in range(20):
        screen.blit(random.choice(die_roll_animation_list),(location))
        time.sleep(0.05)
        pygame.display.flip()


# input hand, returns number of cards that are face up
        
def check_face_up_cards(player_hand):
    face_up_count = 0
    for card in player_hand:
        if card.face_up:
            face_up_count += 1
    return(face_up_count)


#set P1 image locations
image_location = []
for i in range(6):
    image_location.append(((P1_INITIAL_IMAGE_LOCATION_X + (i * CARD_SPACING_X)), P1_IMAGE_LOCATION_Y))

def main():
    deal_button = Button(SCREEN_CENTRE_X - 60, 300, deal_image)
    deal_button.draw(screen)
    roll_button = Button(SCREEN_CENTRE_X - 60, 250, roll_image)
    roll_button.draw(screen)
    pygame.display.flip()
    deck = Deck()
    player1 = Player()

    running = True
    while running: #run until quit
        if roll_button.draw(screen):
            die_roll_animation(P1_DIE_LOCATION)
            global number_of_cards
            number_of_cards = random.randint(1,6)
            die_face = pygame.image.load(f'images\dice\dice-six-faces-{number_of_cards}.png').convert_alpha()
            screen.blit(die_face,(P1_DIE_LOCATION))
            pygame.display.flip()
        
        #check if dealer button clicked and assign cards to player hand
        if deal_button.draw(screen):
            screen.fill(bg_colour) #clear existing cards before dealing new cards
            screen.blit(die_face,(P1_DIE_LOCATION))
            # for i in range(number_of_cards):
             # display discard buttons below cards - CAN'T CURRENTLY CLICK DISCARD BUTTON
                # discard_button = Button((P1_INITIAL_IMAGE_LOCATION_X + (SCALED_IMAGE_SIZE[0]/2) - 44) + (i * CARD_SPACING_X), (P1_IMAGE_LOCATION_Y + SCALED_IMAGE_SIZE[1] + 10), discard_image) #add discard button underneath each card
                # discard_button.draw(screen)
            
            player1.hand = []
            pygame.display.flip()
            for i in range(number_of_cards):
                if len(deck.deck) > 0:
                    player1.hand.append(deck.deal_card())
        
        player_1_discard_button = Button((P1_INITIAL_IMAGE_LOCATION_X + (SCALED_IMAGE_SIZE[0]/2) - 44), (P1_IMAGE_LOCATION_Y + SCALED_IMAGE_SIZE[1] + 10), discard_image) #add discard button underneath each card
        # check number of cards that are face up
        if check_face_up_cards(player1.hand) < 3 and len(player1.hand) > 0:
            player_1_discard_button.draw(screen)

        if check_face_up_cards(player1.hand) > 2 and len(player1.hand) > 0:
            player_1_discard_button.hide(screen, bg_colour)


        # face_up_count = 0
        # for card in player1.hand:
        #     if card.face_up:
        #         face_up_count += 1
        # print(face_up_count)


        #display card images for player hand
        for count, card in enumerate(player1.hand):
            card.show(image_location[count], screen, SCALED_IMAGE_SIZE, bg_colour)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                running = False

if __name__ == "__main__":
    main()