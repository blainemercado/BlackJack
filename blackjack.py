
from random import shuffle
from random import randint

# Creating individual Card objects with attrs and methods
class Card(object):
	def __init__(self, suit, value, image=None):
		self.suit = suit
		self.value = value
		self.image = image

# Creating Deck of Cards along with its attrs and methods
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
		self.shuffle()
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

# Creating Player class
class Player(object):
	def __init__(self, position):
		self.position = position
		self.hand = []
		self.wager = 0
		self.wallet = 100
		
	def bet(self):
		self.wager = randint(1,10)
		self.wallet -= self.wager
		return self

	def hit(self): 
		self.hand.append(deck.deal())
		return self

	def stay(self):
		# game.skip
		pass

	def split(self):
		pass

	def double_down(self):
		self.wallet -= self.wager
		self.wager *= 2
		self.hit()
		self.stay()
		return self


suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
values = range(1,14)

deck = Deck(suits, values)
deck.buildDeck()


# print deck.deck[0].value

player1 = Player(1)

# print player1.position

print player1.wager, player1.wallet
# print player1.wallet
player1.bet()
print player1.wager, player1.wallet
# print player1.wallet


# for cnt in range(0,10):
# 	# print cnt
# 	player1.hit()
# 	print player1.hand[cnt].value


player1.double_down()
print player1.wager, player1.wallet


# print deck.deck[0].value
# print deck.deck[0].suit

# print deck.deck.pop().value

# deck.shuffle()

# print deck.deck[0].value
# print deck.deck[0].suit