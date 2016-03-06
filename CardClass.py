#Bang Card Class

class Card:

    def __init__(self,l1,l2,l3):
        self.card = l1
        self.suit = l2
        self.num = l3

    def getSuit(self):
        return self.suit

    def getNum(self):
        return self.num

    def getCard(self):
        return self.card
