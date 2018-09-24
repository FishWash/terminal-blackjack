from enum import Enum
import time, random

# Change this if you want to see it without the pauses!
pauseOn = True

class Rank(Enum):
    LOWACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def print(self):
        print("["+lookupRankString[self.rank]+lookupSuitString[self.suit]+"]")

class Deck():
    def __init__(self):
        self.cards = []
        for rank in Rank:
            if rank == Rank.LOWACE:
                continue
            for suit in Suit:
                self.cards.append(Card(rank, suit))

    # draw randomly chooses a card from the deck and adds it to otherCards.
    # if deck is empty, does nothing.
    def draw(self, otherCards):
        if (len(self.cards) == 0):
            return
        rand_i = random.randint(0, len(self.cards)-1)
        card = self.cards.pop(rand_i)
        otherCards.append(card)

def printCards(cards):
    for card in cards:
        card.print()

# printCardsHidden prints cards but hides the first one.
def printCardsHidden(cards):
    firstCard = True
    for card in cards:
        if (firstCard):
            print("[??]")
            firstCard = False
            continue
        card.print()

# countPoints returns the total number of points in an array of cards.
def countPoints(cards):
    points = 0
    for card in cards:
        points += rankValueDict[card.rank]

    # If points went above 21, check if any aces can be counted as 1
    if (points > 21):
            for card in cards:
                if card.rank == Rank.ACE:
                    card.rank = Rank.LOWACE
                    return countPoints(cards)
    return points

def dialogue(speaker, message):
    print(">"+speaker+": "+message)
    if pauseOn:
        time.sleep(len(message)*0.01 + 0.4)

def dialogueAction(message):
    print(">"+message)
    if pauseOn:
        time.sleep(0.5)

def dialoguePause():
    if pauseOn:
        time.sleep(0.5)

# inputYesOrNo prompts the user for a yes or no response. Returns true if yes, and false if no.
# Will exit program on specific exit responses.
def inputYesOrNo():
    while (True):
        response = input("    [Y]es/[N]o: ")
        response = response.lower()
        if response in ynResponseDict:
            if (ynResponseDict[response]): 
                return True
            else: 
                return False
        elif (response in exitResponseDict):
            leave()
        else:
            dialogue("You", response + ".")
            dialogue("Dealer", "Uh.. not sure what that means.")

def leave():
    dialogue("Dealer", "See you around.")
    exit()

rankValueDict = {
    Rank.LOWACE: 1,
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4, 
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 10,
    Rank.QUEEN: 10,
    Rank.KING: 10,
    Rank.ACE: 11
}

lookupRankString = {
    Rank.LOWACE: "A",
    Rank.TWO: "2",
    Rank.THREE: "3",
    Rank.FOUR: "4",
    Rank.FIVE: "5",
    Rank.SIX: "6",
    Rank.SEVEN: "7",
    Rank.EIGHT: "8",
    Rank.NINE: "9",
    Rank.TEN: "10",
    Rank.JACK: "J",
    Rank.QUEEN: "Q",
    Rank.KING: "K",
    Rank.ACE: "A"
}

lookupSuitString = {
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
    Suit.HEARTS: "♥",
    Suit.SPADES: "♠"
}

ynResponseDict = {
    "yes": True,
    "y": True,
    "no": False,
    "n": False
}

exitResponseDict = {
    "exit": True,
    "e": True,
    "quit": True,
    "q": True
}

# title card
print()
print("■ ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ ■")
print("♠ _______ _           __    _           __      ♠")
print("· \ ♠___ \ |          \ |  (_)          \ |     ·")
print("♥  |♥|_/ / | __ _  ___| | ___  __ _  ___| | __  ♥")
print("·  |♣___ \ |/ _` |/ __/ |/ / |/ _` |/ __/ |/ /  ·")
print("♣  |♦|_/ / | (_| | (__|   <| | (_| | (__|   <   ♣")
print("· /_____/|_|\__,_\\\\___\_|\_\ |\__,_\\\\___\_|\_\  ·")
print("♦ \______________________ _/ |_______________/  ♦")
print("·                        /__/                   ·")
print("■ ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ · ♦ · ♣ · ♥ · ♠ ■")
print("by Jonathan Fox")

# start game
print("\n([E]xit or [Q]uit at any time will exit the program.)\n\n")
dialogue("Dealer", "Howdy, up for a game of Blackjack?")
if (inputYesOrNo() == True):
    dialogue("You", "Sure.")
else:
    dialogue("You", "Nope.")
    leave()
dialogue("Dealer", "Alright, grab a seat. What's your name?")
name = input("    Enter your name: ")
if (name.lower() in exitResponseDict):
    leave()
dialogue("You", "I'm "+name+".")
dialogue("Dealer", "Pleasure to meet you, "+name+". Let's get started.")

# gameplay loop
while(True):
    deck = Deck()
    print()
    dialogueAction("The dealer shuffles the deck.")

    playerCards = []
    dealerCards = []
    deck.draw(playerCards)
    deck.draw(dealerCards)
    deck.draw(playerCards)
    deck.draw(dealerCards)
    playerFinished = False
    dealerFinished = False

    # turn loop
    while(playerFinished == False or dealerFinished == False):
        # player's turn
        if (playerFinished == False):
            if (countPoints(playerCards) >= 21):
                playerFinished = True
            else:
                print("\nYOUR CARDS:")
                printCards(playerCards)
                print("\nDEALER'S CARDS:")
                printCardsHidden(dealerCards)
                print()
                dialoguePause()
                dialogue("Dealer", "Hit?")
                if (inputYesOrNo() == True):
                    deck.draw(playerCards)
                    dialogueAction("You hit.")
                else:
                    playerFinished = True
                    dialogueAction("You stand.")

        # dealer's turn
        if (dealerFinished == False):
            if (countPoints(dealerCards) >= 17):
                dealerFinished = True
                dialogueAction("The dealer stands.")
            else:
                deck.draw(dealerCards)
                dialogueAction("The dealer hits.")

    playerPoints = countPoints(playerCards)
    dealerPoints = countPoints(dealerCards)

    print("\nYOUR CARDS:")
    printCards(playerCards)
    print("Points: " + str(playerPoints))
    print("\nDEALER'S CARDS:")
    printCards(dealerCards)
    print("Points: " + str(dealerPoints))
    print()
    dialoguePause()

    # game results dialogue
    if playerPoints > 21:
        if dealerPoints > 21:
            dialogue("Dealer", "Hah! we both busted.")
        else:
            dialogue("Dealer", "You busted, I win!")
    elif dealerPoints > 21:
        dialogue("Dealer", "Darn, that's a bust. Guess you win.")

    elif playerPoints > dealerPoints:
        if playerPoints == 21 and len(playerCards) == 2:
            dialogue("Dealer", "Wow, you got a blackjack! Nicely done, "+name+".")
        else:
            dialogue("Dealer", "You win, "+name+".")
    elif (playerPoints == dealerPoints):
        if playerPoints == 21 and len(playerCards) == 2 and dealerPoints == 21 and len(dealerCards) == 2:
            dialogue("Dealer", "Aha! I got blackj- oh, you do too...")
        else:
            dialogue("Dealer", "We're tied, "+name+". How exciting.")
    elif playerPoints < dealerPoints:
        if dealerPoints == 21 and len(dealerCards) == 2:
            dialogue("Dealer", "Blackjack! I win this one.")
        else:
            dialogue("Dealer", "Too bad, "+name+", looks like I win.")

    dialogue("Dealer", "Play again?")
    if (inputYesOrNo() == False):
        leave()