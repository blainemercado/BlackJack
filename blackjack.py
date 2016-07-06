
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
		self.handValue = 0
		self.wager = 0
		self.wallet = 100

	'''def makeChoice(self):
        # if (sumCardValues())
        	self.playerchoice = raw_input("Enter choice: hit, stay or double_down.")
        if self.playerchoice == "hit":
            self.hit()
        elif self.playerchoice == "stay":
            self.stay()
        elif self.playerchoice == "double_down":
            self.double_down()'''

	def bet(self):
		self.wager = randint(1,10)
		self.wallet -= self.wager
		return self

	def hit(self): 
		self.hand.append(deck.deal())
		self.handValue = 0
		self.sumCardValues()
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

	def sumCardValues(self):
		for element in self.hand:
			self.handValue += element.value
		return self

class Dealer(object):
	def __init__(self, position):
		self.position = position
		self.hand = []
		self.handValue = 0

	def hit(self): 
		self.hand.append(deck.deal())	
		return self

	def stay(self):
		# game.skip
		pass

	def sumCardValues(self):
		for element in self.hand:
			self.handValue += element.value
		return self.handValue
		return self

class Game(object):
	def __init__(self):
		self.deckTotal = 52
		#self.dealerHits()
		#self.dealer = Dealer(3)
		self.askBets()
	'''def Turn(self):
		self.dealerHits()'''

	def askBets(self):
		player1.bet()
		player2.bet()
		self.dealPlayers()
		return self

	def dealPlayers(self):
		player1.hand.append(deck.deal())
		player2.hand.append(deck.deal())
		dealer.hand.append(deck.deal())	
		player1.hand.append(deck.deal())
		player2.hand.append(deck.deal())
		dealer.hand.append(deck.deal())
		player1.sumCardValues()
		player2.sumCardValues()
		dealer.sumCardValues()

	def playerAction(self):
		player1.makeChoice()
		player2.makeChoice()

	def dealerHits(self):	
		if 0 < dealer.sumCardValues() < 17:
			dealer.hand.append(deck.deal())
		else:
			print "I'm staying"
			#self.stay()

	


	'''def startGame(self):
		suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
		values = range(1,12)
		deck = Deck(suits, values)
		return self'''

	#initiates the deck


	#ask players to make a decision(hit, stay, split, double_down)
	#ask Dealer to make (auto)decision
	#check scores and declare winners/losers
	#add winnings to winners wallet
	#check number of cards in deck, if less than x (players * 7) deck.resetDeck()

		

suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
values = range(1,12)

deck = Deck(suits, values)
player1 = Player(1)
player2 = Player(2)

dealer = Dealer(3)
BlackJack = Game()

#dealer = Dealer(3)
print "Moneys:", player1.wallet, "Your hand:", player1.handValue
print "Dealer hand:", dealer.handValue
player1.hit()
print "Moneys:", player1.wallet, "Your hand:", player1.handValue
print player1.hand
print player1.hand[0].value, player1.hand[1].value, player1.hand[2].value

'''player1.bet()
print player1.wager, player1.wallet, player1.hand
player1.double_down()
print player1.wager, player1.wallet, player1.hand'''



