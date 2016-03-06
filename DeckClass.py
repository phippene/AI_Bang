#Bang Deck Class

file = "BangDeck.txt"
from CardClass import Card
from random import randrange

class Deck:

    def __init__(self):
        self.drawDeck = []
        self.discardDeck = []
        f = open(file)
        for line in range(80):
            l1 = f.readline().rstrip()
            l2 = f.readline().rstrip()
            l3 = f.readline().rstrip()
            c = Card(l1, l2, l3)
            self.drawDeck.append(c)
            
    def draw(self):
        if len(self.drawDeck) == 0:
            self.shuffleAll()
        r = randrange(0,len(self.drawDeck),1)
        c = self.drawDeck[r]
        self.drawDeck.remove(c)
        return c

    def drawDiscard(self):
        if len(self.discardDeck) == 0:
            return False
        c = self.discardDeck[-1] #last card discarded
        self.discardDeck.remove(c)
        return c

    def discard(self, c):
        self.discardDeck.append(c)

    def shuffleAll(self): #reset all cards to drawDeck
        for card in self.discardDeck:
            self.drawDeck.append(card)
            self.discardDeck.remove(card)
            
    def resetDeck(self):
        self.drawDeck = []
        self.discardDeck = []
        f = open(file)
        for line in f:
            l = (f.readline())
            c = Card(l)
            self.drawDeck.append(c)
