#Board Class
# tracks each player's health, as well as status/gun cards played on the board

from CardClass import Card
from random import randrange

class BoardsBang:

    roles = [["Sheriff",False],["Renegade",False],["Outlaw",False],
            ["Outlaw",False],["Deputy",False],["Outlaw",False],
            ["Deputy",False]]
    role = []
    health = []
    mustang = []
    scope= []
    barrel = []
    dynamite = []
    jail= []
    gun = []
    volcanic = []
        
    #takes in the number of players and fills the neccessary lists
    def __init__(self,numPlayers):

        x = 0
        while x < numPlayers:
            #set random roles
            r = randrange(0,numPlayers,1)
            while self.roles[r][1] == True:
                r = randrange(0,numPlayers,1)
            self.roles[r][1] = True
            self.role.append(self.roles[r][0])
            
            #set health
            if self.role[x] == "Sheriff":
                self.health.append(5)
            else: self.health.append(4)
            #set horse through jail to false and no card
            self.mustang.append([False,None])
            self.scope.append([False,None])
            self.barrel.append([False,None])
            self.dynamite.append([False,None])
            self.jail.append([False,None])
            #set gun to none and volcanic to false
            self.gun.append([1,None])
            self.volcanic.append(False)
            x += 1

    #takes in a player number of who will get gun and a gun card to be played
    #returns true if gun placed and false if card not a gun
    def playGun(self,playerNum,c):
        if c.getCard() == "volcanic":
            self.gun[playerNum][0] = 1
            self.gun[playerNum][1] = c
            self.volcanic[playerNum] = True
            return True
        elif c.getCard() == "schofield":
            self.gun[playerNum][0] = 2
            self.gun[playerNum][1] = c
            self.volcanic[playerNum] = False
            return True
        elif c.getCard() == "remington":
            self.gun[playerNum][0] = 3
            self.gun[playerNum][1] = c
            self.volcanic[playerNum] = False
            return True
        elif c.getCard() == "carabine":
            self.gun[playerNum][0] = 4
            self.gun[playerNum][1] = c
            self.volcanic[playerNum] = False
            return True
        elif c.getCard() == "winchester":
            self.gun[playerNum][0] = 5
            self.gun[playerNum][1] = c
            self.volcanic[playerNum] = False 
            return True
        return False

    #takes in player number of person who will have gun removed
    #returns card if gun removed, and false if no gun present
    def removeGun(self,playerNum):
        if self.gun[playerNum][1] == None:
            return False
        if self.volcanic[playerNum]:
            self.volcanic[playerNum] = False
        self.gun[playerNum][0] = 1
        c = self.gun[playerNum][1]
        self.gun[playerNum][1] = None
        return c
    
    #Returns the gun in hand
    def getGun(self, playerNum):
        if self.gun[playerNum][1] != None:
            return self.gun[playerNum][1]
        else:
            return self.gun[playerNum][1]

    #takes in player number who will get status card and card
    #returns true if card played and false if not status card
    #   or player already has one
    def playStatus(self,playerNum,c):
        if c.getCard() == "barrel" and self.barrel[playerNum][0] == False:
            self.barrel[playerNum][0] = True
            self.barrel[playerNum][1] = c
            return True
        elif c.getCard() == "jail" and self.jail[playerNum][0] == False:
            self.jail[playerNum][0] = True
            self.jail[playerNum][1] = c
            return True
        elif c.getCard() == "dynamite" and self.dynamite[playerNum][0] == False:
            self.dynamite[playerNum][0] = True
            self.dynamite[playerNum][1] = c
            return True
        elif c.getCard() == "mustang" and self.mustang[playerNum][0] == False:
            self.mustang[playerNum][0] = True
            self.mustang[playerNum][1] = c
            return True
        elif c.getCard() == "scope" and self.scope[playerNum][0] == False:
            self.scope[playerNum][0] = True
            self.scope[playerNum][1] = c
            return True
        return False

    #takes in player num of person whose card will be removed, and card name
    #returns card if card removed and false if not a status card or card
    #   not there
    def removeStatus(self,playerNum,cardName):
        if cardName == "barrel" and self.barrel[playerNum][0] == True:
            self.barrel[playerNum][0] = False
            c = self.barrel[playerNum][1]
            self.barrel[playerNum][0] = None
            return c
        elif cardName == "jail" and self.jail[playerNum][0] == True:
            self.jail[playerNum][0] = False
            c = self.jail[playerNum][1]
            self.jail[playerNum][0] = None
            return c
        elif cardName == "dynamite" and self.dynamite[playerNum][0] == True:
            self.dynamite[playerNum][0] = False
            c = self.dynamite[playerNum][1]
            self.dynamite[playerNum][0] = None
            return c
        elif cardName == "mustang" and self.mustang[playerNum][0] == True:
            self.mustang[playerNum][0] = False
            c = self.mustang[playerNum][1]
            self.mustang[playerNum][0] = None
            return c
        elif cardName == "scope" and self.scope[playerNum][0] == True:
            self.scope[playerNum][0] = False
            c = self.scope[playerNum][1]
            self.scope[playerNum][0] = None
            return c
        return False

    #Returns the current status cards on the player
    def getStatus(self,playerNum):
        statusEffects = []
        if self.barrel[playerNum][0]:
            statusEffects.append(self.barrel[playerNum][1])
        if self.jail[playerNum][0]:
            statusEffects.append(self.jail[playerNum][1])
        if self.dynamite[playerNum][0]:
            statusEffects.append(self.dynamite[playerNum][1])
        if self.mustang[playerNum][0]:
            statusEffects.append(self.mustang[playerNum][1])
        if self.scope[playerNum][0]:
            statusEffects.append(self.scope[playerNum[1]])
        return statusEffects
    #takes in player number
    #returns their current health
    def checkHealth(self,playerNum):
        return self.health[playerNum]

    #takes in a player number
    #prints cards on board
    def displayBoard(self,playerNum):
        print("Player ",playerNum,"'s board")
        if self.gun[playerNum][1] == None:
            print("colt.45")
        else:
            print(self.gun[playerNum][1].getCard())
        if self.mustang[playerNum][0]:
            print(self.mustang[playerNum][1].getCard())
        if self.barrel[playerNum][0]:
            print(self.barrel[playerNum][1].getCard())
        if self.scope[playerNum][0]:
            print(self.scope[playerNum][1].getCard())
        if self.dynamite[playerNum][0]:
            print(self.dynamite[playerNum][1].getCard())
        if self.jail[playerNum][0]:
            print(self.jail[playerNum][1].getCard())
            
    #Retunrs Player's Health
    def getHealth(self,playerNum):
        return self.health[playerNum]

    #takes in player number and increases their health by 1
    #returns false if player already dead or at max health
    #returns true if health increased
    def increaseHealth(self,playerNum):
        if self.health[playerNum] > 0:
            if self.role[playerNum] == "Sheriff":
                if self.health[playerNum] == 5:
                    return False
                else:
                    self.health[playerNum] = self.health[playerNum]+1
                    return True
            else:
                if self.health[playerNum] == 4:
                    return False
                else:
                    self.health[playerNum] = self.health[playerNum]+1
                    return True
        return False

    #takes in player number and decreses their health by 1
    #returns true if health decresed and false if already dead
    def decreaseHealth(self,playerNum):
        if self.health[playerNum] > 0:
            self.health[playerNum] -= 1
            return True
        else:
            return False

    #takes in player number and passes dynamite to the next player
    #returns true if pass sucessful, else returns false
    def passDynamite(self, playerNum):
        if(self.dynamite[playerNum][0] == True):
            p = playerNum + 1
            if p == len(self.role):
                p = 0
            self.dynamite[p][0] = True
            self.dynamite[p][1] = self.dynamite[playerNum][1]
            self.dynamite[playerNum][0] = False
            self.dynamite[playerNum][1] = None
            return True
        return False

    #takes in player number and if it is you inquiring
    #returns their role if they are dead or the sheriff, else returns false
    def showRole(self, playerNum, me):
        if self.health[playerNum] == 0 or me:
            return self.role[playerNum]
        elif self.role[playerNum] == "Sheriff":
            return self.role[playerNum]
        else:
            return False

    #takes in your number and the number of the person you want to shoot
    #returns true if you can shoot them
    def canShoot(self,me,other,numPlayers):
        if me == other:
            return False
        distance = self.gun[me][0]
        if self.mustang[other][0]:
            distance -= 1
        if self.scope[me][0]:
            distance += 1
            
        distances = [[1,2,1],[1,2,2,1],[1,2,3,2,1],[1,2,3,3,2,1]]
        
        if me > other:
            index = me - other - 1
        else:
            index = other - me - 1
        meDist = distances[numPlayers-4][index]
        
        if meDist > distance:
            return False;
        
        return True
    
    #takes in your number and the number of the person you want to panic
    #returns true if you can panic them
    def canPanic(self,me,other):
        if me == 0:
            if other == me+1 or other == len(self.role)-1:
                return True
            return False
        elif me == len(self.role)-1:
            if other == 0 or other == me-1:
                return True
            return False
        elif other == me+1 or other == me-1:
            return True
        return False

    #takes in the number of the other person and checks if they are the sheriff
    #returns true if they are not the sheriff
    def canJail(self,other):
        if self.role[other] == "Sheriff":
            return False
        return True 

    #takes in a player number and returns true if they can play
    def canPlay(self,playerNum):
        return self.health[playerNum] > 0

    #takes in playerNum and returns true if in jail
    def inJail(self,playerNum):
        return self.jail[playerNum][0]

    #takes in playerNum and returns true if has dynamite
    def hasDynamite(self,playerNum):
        return self.dynamite[playerNum][0]

    def gunIsVolcanic(self,playerNum):
        if self.volcanic[playerNum]:
            return True
        else:
            return False
        
    def hasMustang(self,pNum):
        return self.mustang[pNum][0]
    
    def hasBarrel(self,pNum):
        return self.barrel[pNum][0]
        
    def hasScope(self,pNum):
        return self.scope[pNum][0]
    
    #returns winning group or None if no winner
    def Winner(self):
        dead = [0,0,0,0] #sheriff,outlaws,renegade,deputys
        for r in range(len(self.role)): #cycle through players
            if self.health[r] == 0:
                if self.role[r] == "Sheriff":
                    dead[0] = dead[0]+1
                elif self.role[r] == "Outlaw":
                    dead[1] = dead[1]+1
                elif self.role[r] == "Renegade":
                    dead[2] = dead[2]+1
                elif self.role[r] == "Deputy":
                    dead[3] = dead[3]+1
                    
        if len(self.role) == 4:
            if dead[0] == 1 and dead[1] < 2:
                self.displayResults()
                #sheriff dead & 1+ outlaw alive
                return "Outlaws"
            elif dead[0] == 1 and dead[1] == 2 and dead[2] == 0:
                self.displayResults()
                #sheriff & outlaws dead, renegade alive
                return "Renegade"
            elif dead[0] == 0 and dead[1] == 2 and dead[2] == 1:
                self.displayResults()
                #sheriff alive, outlaws & renegade dead
                return "Sheriff"
            else: return None
            
        elif len(self.role) == 5: # +1 deputy
            if dead[0] == 1 and dead[1] < 2:
                #sheriff dead & 1+ outlaw alive
                self.displayResults()
                return "Outlaws"
            elif dead[0] == 1 and dead[1] == 2 and dead[2] == 0 and dead[4] == 1:
                #sheriff & outlaws & deputy dead, renegade alive
                self.displayResults()
                return "Renegade"
            elif dead[0] == 0 and dead[1] == 2 and dead[2] == 1:
                #sheriff alive, outlaws & renegade dead
                self.displayResults()
                return "Sheriff/Deputy"
            else: return None
            
        elif len(self.role) == 6: # +1 outlaw & +1 deputy
            if dead[0] == 1 and dead[1] < 3:
                #sheriff dead & 1+ outlaw alive
                self.displayResults()
                return "Outlaws"
            elif dead[0] == 1 and dead[1] == 3 and dead[2] == 0 and dead[4] == 1:
                #sheriff & outlaws & deputy dead, renegade alive
                self.displayResults()
                return "Renegade"
            elif dead[0] == 0 and dead[1] == 3 and dead[2] == 1:
                #sheriff alive, outlaws and renegade dead
                self.displayResults()
                return "Sheriff/Deputy"
            else: return None
            
        elif len(self.role) == 7: # +1 outlaw & +2 deputy
            if dead[0] == 1 and dead[1] < 3:
                #sheriff dead & 1+ outlaw alive
                self.displayResults()
                return "Outlaws"
            elif dead[0] == 1 and dead[1] == 3 and dead[2] == 0 and dead[4] == 2:
                #sheriff & outlaws & deputies dead, renegade alive
                self.displayResults()
                return "Renegade"
            elif dead[0] == 0 and dead[1] == 3 and dead[2] == 1:
                #sheriff alive, outlaws & renegade dead
                self.displayResults()
                return "Sheriff/Deputies"
            else: return None
                   
        return False

    def displayResults(self):
        print("\n")
        for i in range(len(self.role)):
                print("Player:",i,"Role:",self.role[i],"Health:",self.health[i])
        return

    def getSheriffHealth(self):
        for r in range(len(self.role)):
            if self.role[r] == "sheriff":
                return self.health[r]
        