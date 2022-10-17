import random

class Card:
    def __init__(self, value, face, suit):
        self.value = value
        self.face = face
        self.suit = suit
        self.face_up = False

    def __str__(self):
        return f'{self.face if self.face else self.value} of {self.suit} has a value of {self.value} and is {"face up" if self.face_up else "face down"}'


suits = ['hearts', 'spades', 'clubs', 'diamonds']
deck = []
faces = {
    11: 'Ace',
    12: 'Jack',
    13: 'Queen',
    14: 'King'
}


for suit in suits:
    for i in range(1, 15):
        card = None
        if i <= 10:
            card = Card(i, None, suit)
        else:
            face = faces[i]
            value = 11 if face == 'Ace' else 10
            card = Card(value, face, suit)
        deck.append(card)

random.shuffle(deck)
for card in deck:
    print(card)

        
