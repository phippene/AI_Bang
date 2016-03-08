#player class
#Players must be numbered sequentially from 0 to at most 6 with no duplicates

from CardClass import Card

class PlayerBang:

    #constructs character from playerNum, role, starting hand, and playerType
    #character attribute not used at this time
    def __init__(self, pNum, r, h, t):
        self.playerNum = pNum
        self.role = r
        self.hand = h
        self.pType = t
        self.character = None

    #takes in a list of cards and adds them to the hand    
    def addToHand(self,cards):
        for c in cards:
            self.hand.append(c)

    #returns the current hand size
    def handSize(self):
        return len(self.hand)

    #takes in location of card in hand
    #returns card to be discarded or played
    def getFromHand(self,cardLoc):
        c = self.hand[cardLoc]
        self.hand.remove(self.hand[cardLoc])
        return c

    #prints hand
    def displayHand(self):
        print("Player ",self.playerNum,"'s Hand")
        i = 0
        for card in self.hand:
            print(i,": ",card.getCard())
            i = i+1

    #returns hand list
    def retHand(self):
        return self.hand
    
    #returns their playerNum
    def getPlayerNum(self):
        return self.playerNum

    #returns player type
    def getType(self):
        return self.pType
        
    #Remove a given card from the hand
    def removeFromHand(self, c):
        self.hand.remove(c)

    #Adds one card to hand
    def addOneToHand(self, card):
        self.hand.append(card)
        
    def getRole(self):
        return self.role