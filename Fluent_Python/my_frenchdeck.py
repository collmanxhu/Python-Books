from frenchdeck import FrenchDeck, Card, card_02


beer_card = Card('7', 'diamonds')
print(beer_card)
print(len(beer_card))

card_two = card_02(rank=8, suit='clubs')
print(card_two)

card_two = card_02(10, 'spades')
print(card_two)

deck = FrenchDeck()
print(len(deck))
print(deck._cards)
print(len(deck._cards))
print(deck[0])
print(deck[-1])
print(deck[12])
print(deck[:3])
print(deck[12::13])

from random import choice
print(choice(deck))

for card in deck:
    print(card)

print(Card('K', 'hearts') in deck)
print(Card('K', 'tearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)