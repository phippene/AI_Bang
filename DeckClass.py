#Bang Deck Class

file = 'D:\AI\AI_Bang\BangDeck.txt
import Card
import Random

class Deck:

    deck = []
    def _init_(self):
        f = open(file)
        for line in f:
            l = (f.readline())
            c = Card(l)
            deck.append(c)
            
    def draw(self):
        r = randrange(0,deck.len(),1)
        while deck[r].isDrawn():
            r = randrange(0,deck.len(),1)
        deck[r].draw()
        return deck[r]

    def discard(self, c):
        found = False;
        while

    def shuffleAll(self): #reset all cards to undrawn
        for card in deck:
            card.discard()
