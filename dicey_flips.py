import pygame
import sys
from deck import Deck
from player import Player
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
P2_DIE_LOCATION = (0, 0)
P3_DIE_LOCATION = (100, 100)

player_list = []

player1 = Player((P1_INITIAL_IMAGE_LOCATION_X, P1_IMAGE_LOCATION_Y))
player_list.append(player1)

player2 = Player((P1_INITIAL_IMAGE_LOCATION_X, P1_IMAGE_LOCATION_Y - 225))
player_list.append(player2)

player3 = Player((P1_INITIAL_IMAGE_LOCATION_X, P1_IMAGE_LOCATION_Y - 450))
player_list.append(player3)

number_of_cards = 0

discard_image = pygame.image.load('images\\buttons\\discard.png').convert_alpha()
deal_image = pygame.image.load('images\\buttons\\deal.png').convert_alpha()
roll_image = pygame.image.load('images\\buttons\\roll.png').convert_alpha()
#card_back = pygame.image.load('images\\cards\\card_back.png').convert_alpha()

# create list of randome die face images
die_roll_animation_list = []
for i in range(1,6):
    die_roll_animation_list.append(pygame.image.load(f'images\dice\dice-six-faces-{i}.png').convert())
    
def die_roll_animation(location):
    for i in range(20):
        screen.blit(random.choice(die_roll_animation_list),(location))
        time.sleep(0.05)
        pygame.display.flip()


def show_player_cards(hand, location_list, surface, colour):
    for count, card in enumerate(hand):
        card.show(location_list[count], surface, colour)
        pygame.display.flip()

# input hand, returns number of cards that are face up
def check_face_up_cards(player_hand):
    face_up_count = 0
    for card in player_hand:
        if card.face_up:
            face_up_count += 1
    return(face_up_count)


#set P1 image locations
# image_location = []
# for i in range(6):
#     image_location.append(((P1_INITIAL_IMAGE_LOCATION_X + (i * CARD_SPACING_X)), P1_IMAGE_LOCATION_Y))


def show_all_dice(player_list, screen):
    for player in player_list:
        try:
            screen.blit(player.die_face,(player.die_location)) # add die faces back onto screen
            pygame.display.update()
        except:
            pass
def main():

    for player in player_list:

        #create buttons
        player.deal_button = Button(player.initial_x -50, player.inital_y + 50, deal_image) # set deal button for each player
        # player.deal_button.draw(screen)
        player.roll_button = Button(player.initial_x - 50, player.inital_y + 100, roll_image) # set roll button for each player
        player.roll_button.draw(screen)
        player.discard_button = Button((player.initial_x - 30), (player.inital_y + SCALED_IMAGE_SIZE[1] + 10), discard_image) #add discard button

        # create player card locations
        for i in range(6):
            player.card_locations.append(((player.initial_x + 100 + (i * CARD_SPACING_X)), player.inital_y))

    # def show_all_dice(player_list, screen):
    #     for player in player_list:
    #         screen.blit(player.die_face,(player.die_location)) # add die faces back onto screen
    #         pygame.display.update()

    pygame.display.flip()
    deck = Deck() # create shuffled deck of cards

    running = True
    while running: #run until quit

        for player in player_list:
            if player.roll_button.draw(screen):

                player.no_of_cards = random.randint(1,6)

                die_roll_animation(player.die_location)
                player.die_face = pygame.image.load(f'images\dice\dice-six-faces-{player.no_of_cards}.png').convert_alpha()
                show_all_dice(player_list, screen)
                pygame.display.update()
            
            #check if dealer button clicked and assign cards to player hand
                
            if player.no_of_cards > 0:
                if player.deal_button.draw(screen):
                    screen.fill(bg_colour) #clear existing cards before dealing new cards
                    # screen.blit(player.die_face,(player.die_location))
                    show_all_dice(player_list, screen)

                    
                    player.hand = []
                    pygame.display.flip()
                    for i in range(player.no_of_cards):
                        if len(deck.deck) > 0:
                            player.hand.append(deck.deal_card())

            
            # check number of cards that are face up and display discard button
            if check_face_up_cards(player.hand) < 3 and len(player.hand) > 2:
                if player.discard_button.draw(screen):
                    while len(player.hand) > 2:
                        for card in player.hand:
                            if card.face_up == False:
                                card.face_up = True
                                player.hand.remove(card) # remove card from player hand
                                deck.deck.append(card) # put card back in deck
                    deck.shuffle() # shuffle deck

                    # for card in deck.deck:
                    #     card.print_card()

                    print(len(deck.deck))
                    screen.fill(bg_colour)
                    show_player_cards(player.hand, player.card_locations, screen, bg_colour)
                    show_all_dice(player_list, screen)
                    # for player in player_list:
                    #     screen.blit(player.die_face,(player.die_location)) # add die faces back onto screen
                    #     pygame.display.update()


            if check_face_up_cards(player.hand) > 2 and len(player.hand) > 0:
                player.discard_button.hide(screen, bg_colour)

            #display card images for player hand
            show_player_cards(player.hand, player.card_locations, screen, bg_colour)

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                running = False

if __name__ == "__main__":
    main()