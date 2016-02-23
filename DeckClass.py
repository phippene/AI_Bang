#Bang Deck Class

file = 'D:\AI\AI_Bang\BangDeck.txt
import Card
import Random

class Deck:

    drawDeck = [] #draw pile
    discardDeck = [] #discard pile
    inPlay = [] #cards in play or in hand
    
    def _init_(self):
        f = open(file)
        for line in f:
            l = (f.readline())
            c = Card(l)
            drawDeck.append(c)
            
    def draw(self):
        r = randrange(0,deck.len(),1)
        c = drawDeck[r]
        inPlay.append(c)
        drawDeck.remove(c)
        return c

    def drawDiscard(self):
        c = discardDeck[-1] #last card discarded
        inPlay.append(c)
        discardDeck.remove(c)
        return c

    def discard(self, c):
        discardDeck.append(c)
        inPlay.remove(c)

    def shuffleAll(self): #reset all cards to drawDeck
        for card in discardDeck:
            drawDeck.append(card)
        for card in inPlay:
            drawDeck.append(card)
            
