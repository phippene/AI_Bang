#player class
#Players must be numbered sequentially from 0 to at most 6 with no duplicates

import Card

class PlayerBang:

    #constructs character from playerNum, role, starting hand, and playerType
    #character attribute not used at this time
    def _init_(self, pNum, r, h, t):
        playerNum = pNum
        role = r
        hand = h
        pType = t
        character = None

    #takes in a list of cards and adds them to the hand    
    def addToHand(self,cards):
        for c in cards:
        hand.append(c)

    #returns the current hand size
    def handSize(self):
        return hand.len()

    #takes in location of card in hand
    #returns card to be discarded or played
    def getFromHand(self,cardLoc):
        c = hand[cardLoc]
        hand.remove(hand[cardLoc])
        return c

    #returns list containing hand
    def displayHand(self):
        return hand

    #returns their playerNum
    def getPlayerNum(self):
        return playerNum

    #returns player type
    def getType(self):
        return ptype
    
