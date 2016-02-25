#Board Class
# tracks each player's health, as well as status/gun cards played on the board

import Card
import Random

class BoardsBang:

    role = []
    health = []
    mustang = []
    scope = []
    barrel = []
    dynamite = []
    jail = []
    gun = []

    #takes in the number of players and fills the neccessary lists
    def _init_(self,numPlayers):
        roles = [["Sheriff",False],["Renegade",False],["Outlaw",False],
                ["Outlaw",False],["Deputy",False],["Outlaw",False],
                ["Deputy",False]]
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
            #set horse through jail to false and no card
            horse.append([False,None])
            scope.append([False,None])
            barrel.append([False,None])
            dynamite.append([False,None])
            jail.append([False,None])
            #set gun to none and volcanic to false
            gun.append([1,None])
            volcanic.append(False)

    #takes in a player number of who will get gun and a gun card to be played
    #returns true if gun placed and false if card not a gun
    def playGun(self,playerNum,c):
        if c.getCard() == "volcanic":
            gun[playerNum][0] = 1
            gun[playerNum][1] = c
            return True
        elif c.getCard() == "schofield":
            gun[playerNum][0] = 2
            gun[playerNum][1] = c
            return True
        elif c.getCard() == "remington":
            gun[playerNum][0] = 3
            gun[playerNum][1] = c
            return True
        elif c.getCard() == "carabine":
            gun[playerNum][0] = 4
            gun[playerNum][1] = c
            return True
        elif c.getCard() == "winchester":
            gun[playerNum][0] = 5
            gun[playerNum][1] = c
            return True
        return False

    #takes in player number of person who will have gun removed
    #returns card if gun removed, and false if no gun present
    def removeGun(self,playerNum):
        if gun[playerNum][1] == None:
            return False
        gun[playerNum][0] = 1
        c = gun[playerNum][1]
        gun[playerNum][1] = None
        return c

    #takes in player number who will get status card and card
    #returns true if card played and false if not status card
    #   or player already has one
    def playStatus(self,playerNum,c):
        if c.getCard() == "barrel" && barrel[playerNum][0] == False:
            barrel[playerNum][0] = True
            barrel[playerNum][1] = c
            return True
        elif c.getCard() == "jail" && jail[playerNum][0] == False:
            jail[playerNum][0] = True
            jail[playerNum][1] = c
            return True
        elif c.getCard() == "dynamite" && dynamite[playerNum][0] == False:
            dynamite[playerNum][0] = True
            dynamite[playerNum][1] = c
            return True
        elif c.getCard() == "mustang" && mustang[playerNum][0] == False:
            mustang[playerNum][0] = True
            mustang[playerNum][1] = c
            return True
        elif c.getCard() == "scope" && scope[playerNum][0] == False:
            scope[playerNum][0] = True
            scope[playerNum][1] = c
            return True
        return False

    #takes in player num of person whose card will be removed, and card name
    #returns card if card removed and false if not a status card or card
    #   not there
    def removeStatus(self,playerNum,cardName):
        if cardName == "barrel" && barrel[playerNum][0] = True:
            barrel[playerNum][0] = False
            c = barrel[playerNum][1]
            barrel[playerNum][0] = None
            return c
        elif cardName == "jail" && jail[playerNum][0] = True:
            jail[playerNum][0] = False
            c = jail[playerNum][1]
            jail[playerNum][0] = None
            return c
        elif cardName == "dynamite" && dynamite[playerNum][0] = True:
            dynamite[playerNum][0] = False
            c = dynamite[playerNum][1]
            dynamite[playerNum][0] = None
            return c
        elif cardName == "mustang" && mustang[playerNum][0] = True:
            mustang[playerNum][0] = False
            c = mustang[playerNum][1]
            mustang[playerNum][0] = None
            return c
        elif cardName == "scope" && scope[playerNum][0] = True:
            scope[playerNum][0] = False
            c = scope[playerNum][1]
            scope[playerNum][0] = None
            return c
        return False

    #takes in player number
    #returns their current health
    def checkHealth(self,playerNum):
        return health[playerNum]

    #takes in player number and increases their health by 1
    #returns false if player already dead or at max health
    #returns true if health increased
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

    #takes in player number and decreses their health by 1
    #returns true if health decresed and false if already dead
    def decreaseHealth(self,playerNum):
        if health[playerNum] > 0:
            health[playerNum] -= 1
            return True
        else:
            return False

    #takes in player number and passes dynamite to the next player
    #returns true if pass sucessful, else returns false
    def passDynamite(self, playerNum):
        if(dynamite[playerNum][0] = True):
            p = playerNum + 1
            if p == role.len():
                p = 0
            dynamite[p][0] = True
            dynamite[p][1] = dynamite[playerNum][1]
            dynamite[playerNum][0] = False
            dynamite[playerNum][1] = None
            return True
        return False

    #takes in player number and if it is you inquiring
    #returns their role if they are dead or the sheriff, else returns false
    def showRole(self, playerNum, me = False):
        if health[playerNum] == 0 || me:
            return role[playerNum]
        elif role[playerNum] == "Sheriff":
            return role[PlayerNum]
        else:
            return False

    
    #takes in a player number and returns true if they can play
    def canPlay(self,playerNum):
        return health[playerNum] > 0

    #returns winning group or None if no winner
    def Winner(self):
        dead = [0,0,0,0] #sheriff,outlaws,renegade,deputys
        for r in role: #cycle through players
            if health[r] == 0:
                if role[r] == "Sheriff":
                    dead[0]++
                elif role[r] == "Outlaw":
                    dead[1]++
                elif role[r] == "Renegade":
                    dead[2]++
                elif role[r] == "Deputy":
                    dead[3]++
                    
        if role.len() == 4:
            if dead[0] == 1 && dead[1] < 2:
                #sheriff dead & 1+ outlaw alive
                return "Outlaws"
            elif dead[0] == 1 && dead[1] == 2 && dead[2] == 0:
                #sheriff & outlaws dead, renegade alive
                return "Renegade"
            elif dead[0] == 0 && dead[1] == 2 && dead[2] == 1:
                #sheriff alive, outlaws & renegade dead
                return "Sheriff"
            else: return None
            
        elif role.len() == 5: # +1 deputy
            if dead[0] == 1 && dead[1] < 2:
                #sheriff dead & 1+ outlaw alive
                return "Outlaws"
            elif dead[0] == 1 && dead[1] == 2 && dead[2] == 0 && dead[4] == 1:
                #sheriff & outlaws & deputy dead, renegade alive
                return "Renegade"
            elif dead[0] == 0 && dead[1] == 2 && dead[2] == 1:
                #sheriff alive, outlaws & renegade dead
                return "Sheriff/Deputy"
            else: return None
            
        elif role.len() == 6: # +1 outlaw & +1 deputy
            if dead[0] == 1 && dead[1] < 3:
                #sheriff dead & 1+ outlaw alive
                return "Outlaws"
            elif dead[0] == 1 && dead[1] == 3 && dead[2] == 0 && dead[4] == 1:
                #sheriff & outlaws & deputy dead, renegade alive
                return "Renegade"
            elif dead[0] == 0 && dead[1] == 2 && dead[2] == 1:
                #sheriff alive, outlaws and renegade dead
                return "Sheriff/Deputy"
            else: return None
            
        elif role.len() == 7: # +1 outlaw & +2 deputy
            if dead[0] == 1 && dead[1] < 3:
                #sheriff dead & 1+ outlaw alive
                return "Outlaws"
            elif dead[0] == 1 && dead[1] == 3 && dead[2] == 0 && dead[4] == 2:
                #sheriff & outlaws & deputies dead, renegade alive
                return "Renegade"
            elif dead[0] == 0 && dead[1] == 2 && dead[2] == 1:
                #sheriff alive, outlaws & renegade dead
                return "Sheriff/Deputies"
            else: return None
                   
        return False



