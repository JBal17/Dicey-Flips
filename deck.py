import random

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
        self.discard = False
        self.face_up = True

    def show(self):
        if self.face_up == True:
            return(f'{self.value}_of_{self.suit}')
        elif self.face_up == False:
            return (f'card_back')
        


class Player():
    def __init__(self):
        self.hand = []

def main():
    deck = Deck() #create a deck of cards

    for card in deck.deck:
        print(card.show())

    player1 = Player()



    # for i in range(2):
    #     player1.hand.append(deck.deal_card())

    # print(player1.hand)

if __name__ == "__main__":
    main()