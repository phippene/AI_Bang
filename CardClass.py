#Bang Card Class

class Card:

    def _init_(self,l):
        card = l[0]
        suit = l[1]
        num = l[2]
        drawn = False

    def isDrawn(self):
        return drawn
    
    def draw(self):
        drawn = True
    
    def discard(self):
        drawn = False

    def getSuit(self):
        return suit

    def getNum(self):
        return num

    def getCard(self)
        return card
