#Board Class

import Card
import Deck
import Random

class Boards:

    role = []
    health = []
    mustang = []
    scope = []
    barrel = []
    dynamite = []
    jail = []
    gun = []

    def _init_(self,numPlayers):
        roles = [["Sheriff",False],["Renegade",False],["Outlaw",False],
                ["Outlaw",False],["Deputy",False],["Outlaw",False],
                ["Deputy",False]]
        deck = Deck()
        for x in range(numPlayers):
            #set random roles
            r = randrange(0,numPlayers,1)
            while roles[r][1] == True:
                r = randrange(0,numPlayers,1)
            roles[r][1] = True
            role.append(roles[r][0])
            #set health
            if role[x] == "Sheriff":
                health.append(5)
            else: health.append(4)
            #set horse through jail to false
            horse.append([False,None])
            scope.append([False,None])
            barrel.append([False,None])
            dynamite.append([False,None])
            jail.append([False,None])
            #set gun range and volcanic
            gun.append([1,None])
            volcanic.append(False)
        
    def playGun(self,playerNum,c):
        if c.getCard() == "volcanic":
            gun[playerNum][0] = 1
            gun[playerNum][1] = c
        elif c.getCard() == "schofield":
            gun[playerNum][0] = 2
            gun[playerNum][1] = c
        elif c.getCard() == "remington":
            gun[playerNum][0] = 3
            gun[playerNum][1] = c
        elif c.getCard() == "carabine":
            gun[playerNum][0] = 4
            gun[playerNum][1] = c
        elif c.getCard() == "winchester":
            gun[playerNum][0] = 5
            gun[playerNum][1] = c

    def removeGun(self,playerNum):
        gun[playerNum][0] = 1
        deck.discard(gun[playerNum][1])
        gun[playerNum][1] = None
            
    def playStatus(self,playerNum,c):
        if c.getCard() == "barrel":
            barrel[playerNum][0] = True
            barrel[playerNum][1] = c
        elif c.getCard() == "jail":
            jail[playerNum][0] = True
            jail[playerNum][1] = c
        elif c.getCard() == "dynamite":
            dynamite[playerNum][0] = True
            dynamite[playerNum][1] = c
        elif c.getCard() == "mustang":
            mustang[playerNum][0] = True
            mustang[playerNum][1] = c
        elif c.getCard() == "scope":
            scope[playerNum][0] = True
            scope[playerNum][1] = c

    def removeStatus(self,playerNum,cardName):
        if cardName == "barrel":
            barrel[playerNum][0] = False
            deck.discard(barrel[playerNum][1])
            barrel[playerNum][0] = None
        elif cardName == "jail":
            jail[playerNum][0] = False
            deck.discard(jail[playerNum][1])
            jail[playerNum][0] = None
        elif cardName == "dynamite":
            dynamite[playerNum][0] = False
            deck.discard(dynamite[playerNum][1])
            dynamite[playerNum][0] = None
        elif cardName == "mustang":
            mustang[playerNum][0] = False
            deck.discard(mustang[playerNum][1])
            mustang[playerNum][0] = None
        elif cardName == "scope":
            scope[playerNum][0] = False
            deck.discard(scope[playerNum][1])
            scope[playerNum][0] = None

    def checkHealth(self,playerNum):
        return health[playerNum]

    def increaseHealth(self,playerNum):
        if health[playerNum] > 0:
            if role[playerNum] == "Sheriff":
                if health[playerNum] == 5:
                    return False
                else:
                    health[playerNum]++
                    return True
            else:
                if health[playerNum] == 4:
                    return False
                else:
                    health[playerNum]++
                    return True
        return False
        
    def decreaseHealth(self,playerNum):
        if health[playerNum] > 0:
            health[playerNum] -= 1
            return True
        else:
            return False

    def showRole(self,playerNum):
        if health[playerNum] == 0:
            return role[playerNum]
        elif role[playerNum] == "Sheriff":
            return role[PlayerNum]
        else:
            return False




