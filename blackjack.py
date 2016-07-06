
from random import shuffle

class Card(object):
	def __init__(self, suit, value, image=None):
		self.suit = suit
		self.value = value
		self.image = image


class Deck(object):
	def __init__(self, suits, values):
		self.suits = suits
		self.values = values
		self.deck = []
		self.buildDeck()

	def buildDeck(self):
		for suit in self.suits:
			for value in self.values:
				self.deck.append(Card(suit, value))
		return self

	def shuffle(self):
		shuffle(self.deck)
		return self
	
	def deal(self):
		if self.deck:
			return self.deck.pop()
		else:
			print "No more cards"

	def returnCard(self, card, reshuffle=False):
		self.deck.append(card)
		if reshuffle:
			self.shuffle()
		return self

	def resetDeck(self):
		self.deck = []
		self.buildDeck()
		self.shuffle()
		return self



suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
values = range(1,14)

deck = Deck(suits, values)

print deck.deck[0].value
print deck.deck[0].suit

print deck.deck.pop().value

deck.shuffle()

print deck.deck[0].value
print deck.deck[0].suit