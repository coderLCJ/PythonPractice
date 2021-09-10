import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card[item]

    @property
    def card(self):
        return self._card


deck = FrenchDeck()
print(len(deck))

# sorted
def spade_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
for card in sorted(deck, key=spade_high):
    print(card)
