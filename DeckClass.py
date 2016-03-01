#Bang Deck Class

file = 'D:\AI\AI_Bang\BangDeck.txt
import Card
import Random

class Deck:

    drawDeck = [] #draw pile
    discardDeck = [] #discard pile
    
    def _init_(self):
        f = open(file)
        for line in f:
            l = (f.readline())
            c = Card(l)
            drawDeck.append(c)
            
    def draw(self):
        r = randrange(0,deck.len(),1)
        c = drawDeck[r]
        drawDeck.remove(c)
        return c

    def drawDiscard(self):
        c = discardDeck[-1] #last card discarded
        discardDeck.remove(c)
        return c

    def discard(self, c):
        discardDeck.append(c)

    def shuffleAll(self): #reset all cards to drawDeck
        for card in discardDeck:
            drawDeck.append(card)
            discardDeck.remove(card)
            
    def resetDeck(self):
        drawDeck = []
        discardDeck = []
        f = open(file)
        for line in f:
            l = (f.readline())
            c = Card(l)
            drawDeck.append(c)
