#Bang Game

from BoardClass import BoardsBang
from PlayerClass import PlayerBang
from DeckClass import Deck

class BangGame:

    #takes in number of players and sets up deck, players, and boards 
    def __init__(self, np):
        self.played = False
        self.players = []
        self.guns = ["volcanic","schofield","remington","carabine","winchester"]
        self.meStatus = ["barrel","dynamite","mustang","scope"]

        self.numPlayers = np
        self.deck = Deck()
        self.boards = BoardsBang(np)
        i = 0
        while i < np:
            h = []
            r = self.boards.showRole(i,True)
            h.append(self.deck.draw())
            h.append(self.deck.draw())
            h.append(self.deck.draw())
            h.append(self.deck.draw())
            if r == "Sheriff":
                h.append(self.deck.draw())
            print("What type of player is player ", i)
            t = input("Your choices are human or ai: ")
            while t != "human" and t != "ai":
                print("invalid input")
                t = input("Your choices are human or ai: ")
            p = PlayerBang(i,r,h,t)
            self.players.append(p)
            i = i+1

    #plays a game of Bang
    def Play(self):
        while self.played == False:
            self.played = True
            for player in self.players:
                if self.boards.showRole(player.getPlayerNum(),True) == "Sheriff":
                   turn = player.getPlayerNum()
            while self.boards.Winner() == None:
                if self.players[turn].getType() == "ai": #AI player
                   self.AITurn(turn)
                else: #human player
                    self.HumanTurn(turn)
                turn = turn+1
                if turn == self.numPlayers: #circle back
                   turn = 0
            print(self.boards.Winner())
            self.askPlayAgain()
        return None

    #plays an AI turn for player pNum
    def AITurn(self,pNum):
        #check can play
        if self.boards.canPlay(pNum) == False:
            return None
        print("\nPlayer ",pNum,"'s Turn")
        #check dynamite
        if self.checkDynamite(pNum) == False:
            return None
        #check jail
        if self.checkJail(pNum) == False:
            return None
        #draw 2 cards
        self.startDraw(pNum)
        #play cards
        return None

    #plays a human turn for player pNum
    def HumanTurn(self,pNum):
        #check can play
        if self.boards.canPlay(pNum) == False:
            return None
        print("\nPlayer ",pNum,"'s Turn")
        print("Player ",pNum,"'s Health: ", self.boards.getHealth(pNum))
        #check dynamite
        if self.checkDynamite(pNum) == False:
            return None
        #check jail
        if self.checkJail(pNum) == False:
            return None
        #draw 2 cards
        self.startDraw(pNum)
        #play cards
        canPlayBang = True
        while self.players[pNum].handSize() > 0 and self.boards.canPlay(pNum):
            result = False
            while result == False:
                cnum = self.humanPickCard(pNum)
                if cnum < 0:
                    self.discardExtra(pNum)
                    return None
                else:
                    c = self.players[pNum].getFromHand(cnum)
                    result = self.humanPlayCard(pNum,c,canPlayBang)
                    if result == True and c.getCard() == "bang":
                        canPlayBang = False
                    if result == False:
                        self.players[pNum].addOneToHand(c)
        self.discardExtra(pNum)
        return None

    def humanPlayCard(self,pNum,c,canPlayBang):
        cname = c.getCard()
        if cname in self.guns:
            if self.boards.playGun(pNum,c) == False:
                print("error")
                return False
            else:
                self.boards.playGun(pNum,c)
        elif cname in self.meStatus:
            if self.boards.playStatus(pNum,c) == False:
                print("you already have one of those")
                return False
        elif cname == "bang":
            if canPlayBang == True or self.boards.gunIsVolcanic(pNum):
                print("attempting shot")                
                if self.shootOne(pNum,c) == False:
                    print("can't shoot that person!")
                    return False #Couldn't shoot that person
                return True
            print("You may use a Bang once per turn")
            return False
        elif cname == "duel":
            if self.duel(pNum,c) == False:
                return False
        elif cname == "panic":
            if self.panicCatBalou(pNum,True,c) == False:
                return False
        elif cname == "cat balou":
            if self.panicCatBalou(pNum,False,c) == False:
                return False
        elif cname == "jail":
            opp = int(input("which player would you like to put in jail: "))
            if self.boards.canJail(opp) == True:
                if self.boards.playStatus(opp,c) == False:
                   print("They are already in Jail")
        elif cname == "indians":
            self.shootAll(pNum,True,c)
        elif cname == "gatling":
            self.shootAll(pNum,False,c)
        elif cname == "general store":
            self.generalStore(pNum,c)
        elif cname == "wells fargo":
            draw = [self.deck.draw(),self.deck.draw(),self.deck.draw()]
            self.players[pNum].addToHand(draw)
        elif cname == "stagecoach":
            draw = [self.deck.draw(),self.deck.draw()]
            self.players[pNum].addToHand(draw)
        elif cname == "beer":
            if self.boards.increaseHealth(pNum) == False:
                print("your health is already full")
                return False
        elif cname == "saloon":
            for i in range(self.numPlayers):
                self.boards.increaseHealth(pNum)
        elif cname == "missed":
            print("you cant play a 'missed' now")
            return False
        else:
            return False
        return True

    def duel(self,pNum,c):
        opp = int(input("who would you like to duel: "))
        while opp == pNum or opp >= self.numPlayers or opp < 0:
            print("Invalid player Number (enter -1 to retract card")
            opp = int(input("Please pick another Player: "))
            if opp == -1:
                return False
            self.deck.discard(c)
        again = False
        while again == False:
            if self.bangResponse(opp) == False:
                return True
            if self.bangResponse(pNum) == False:
                return True
        
    def panicCatBalou(self,pNum,panic,c):
        if panic:
            cp = False
            while cp == False:
                opp = int(input("Who would you like to panic: "))
                if opp == -1:
                        return False
                while opp == pNum or opp >= self.numPlayers or opp < 0:
                    print("Invalid player Number (enter -1 to retract card)")
                    opp = int(input("Please pick another Player: "))
                    if opp == -1:
                        return False
                cp = self.boards.canPanic(pNum,opp)
                if cp == False:
                    print("That player is out of range (enter -1 to retract card) ")
                    print("Please pick another Player")
            self.boards.displayBoard(opp)
            steal = int(input("Which card would you like to steal: "))
            c2 = self.boards.removeStatus(opp,steal)
            if c2 == False:
                c2 = self.boards.removeGun(opp)
                if c2 == False:
                    stealable = False
                else:
                    stealable = True
            while stealable == False:
                print("Invalid card (enter -1 to retract card)")
                steal = int(input("Please pick another card to steal: "))
                if steal == -1:
                    return False
                if steal != "colt.45":
                    stealable = True
                c2 = self.boards.removeStatus(opp,steal)
                if c2 == False:
                    c2 = self.boards.removeGun(opp)
                    if c2 == False:
                        stealable = False
                    else:
                        stealable = True
            self.players[pNum].addOneToHand(c2)
            self.deck.discard(c)
            return True                        
        else:
            opp = int(input("Who would you like to cat balou: "))
            while opp == pNum or opp >= self.numPlayers or opp < 0:
                print("Invalid player Number (enter -1 to retract card")
                opp = int(input("Please pick another Player: "))
                if opp == -1:
                    return False
            self.boards.displayBoard(opp)
            cb = int(input("Which card would you like to cat balou (-1 to retract card): "))
            while cb < 0:
                print("boom")
                return False
            c2 = self.boards.removeStatus(opp,cb)
            if c2 == False:
                c2 = self.boards.removeGun(opp)
                if c2 == False:
                    cbable = False
                else:
                    cbable = True
            while cbable == False:
                print("Invalid card (enter -1 to retract card) ")
                cb = int(input("Please pick another card to cat balou: "))
                if cb == -1:
                    return False
                if cb != "colt.45":
                    cbable = True
                c2 = self.boards.removeStatus(opp,cb)
                if c2 == False:
                    c2 = self.boards.removeGun(opp)
                    if c2 == False:
                        cbable = False
                    else:
                        cbable = True 
            self.deck.discard(c)
            self.deck.discard(c2)
            return True
                      
    def generalStore(self,pNum,c):
        self.deck.discard(c)
        avail = []
        for i in range(self.numPlayers):
            avail.append(self.deck.draw())
        circle = False
        start = pNum
        loc = pNum
        end = pNum-1
        if end < 0:
            end = self.numPlayers-1
        while circle == False:
            print("Player ",loc)
            i = 0
            for card in avail:
                print(i,": ",card.getCard())
                i = i+1
            c = int(input("which card would you like to take: "))
            while c not in range(len(avail)):
                print("invalid card")
                c = int(input("which card would you like to take: "))
            choice = []
            choice.append(avail[c])
            avail.remove(choice[0])
            self.players[loc].addToHand(choice)
            if loc != start:
                self.discardExtra(loc)
            loc = loc+1
            if loc == self.numPlayers:
                loc = 0
            if loc == start:
                circle = True
        return True
                    
            
    def discardExtra(self,pNum):
        while self.players[pNum].handSize() > self.boards.checkHealth(pNum):
            self.players[pNum].displayHand()
            print("Your health is ",self.boards.getHealth(pNum)," so your hand size is too big!")
            c = int(input("Which card would you like to discard? "))
            card = self.players[pNum].getFromHand(c)
            self.deck.discard(card)
        return True
            
    def missedResponse(self,oppNum):
        h = self.players[oppNum].retHand()
        for c in h:
            if c.getCard() == 'missed':
                print("would player ",oppNum," like to play a missed?")                
                use = input("(y/n): ")
                if use == "y":
                    self.players[oppNum].removeFromHand(c)
                    self.deck.discard(c)
                    return True
                else:
                    self.boards.decreaseHealth(oppNum)
                    print("Player ",oppNum," was shot!")
                    return False
        self.boards.decreaseHealth(oppNum)
        print("Player ",oppNum," was shot!")
        return False
                         
    def bangResponse(self,oppNum):
        h = self.players[oppNum].retHand()
        for c in h:
            if c.getCard() == 'bang':
                print("Would player ",oppNum," like to play a Bang?")
                use = input("(y/n): ")
                if use == "y":
                    self.players[oppNum].removeFromHand(c)
                    self.deck.discard(c)
                    return True
                else:
                    self.boards.decreaseHealth(oppNum)
                    print("Player ",oppNum," was shot!")
                    return False
        self.boards.decreaseHealth(oppNum)
        return False
                         
    def shootAll(self,pNum,indians,c):
        if indians:
            for p in range(self.numPlayers):
                if p != pNum:
                    self.bangResponse(p)
        else:
            for p in range(self.numPlayers):
                if p != pNum:
                    self.missedResponse(p)
        self.deck.discard(c)
        return True
                         
    def shootOne(self,pNum,c):
        opp = int(input("Who would you like to shoot: "))
        cs = False
        while cs == False:
            while opp == pNum or opp >= self.numPlayers or opp < 0:
                print("Invalid player Number (enter -1 to retract card)")
                opp = int(input("Please pick another Player: "))
                if opp == -1:
                    return False
            cs = self.boards.canShoot(pNum,opp,self.numPlayers)
            if cs == False:
                print("That player is out of range (enter -1 to retract card)")
                opp = int(input("Please pick another Player: "))
                if opp == -1:
                    return False
        print("gonna shoot a person")
        self.missedResponse(opp)
        self.deck.discard(c)
        return True
                                    
    def humanPickCard(self,pNum):
        self.players[pNum].displayHand()
        cnum = int(input("Which card would you like to play (-1 to end your turn): "))
        return cnum

    #takes in player number and draws two cards
    def startDraw(self,pNum):
        c = [self.deck.draw(), self.deck.draw()]
        self.players[pNum].addToHand(c)
        return None
        
    #takes in player number and checks if they are in jail
    #returns true if they get out and false if they are suck
    def checkJail(self,pNum):
        if self.boards.inJail(pNum):
            print("Player ",pNum," is in Jail and must draw a heart to play!")
            c = self.deck.draw()
            print("Player ",pNum," drew a ",c.getSuit())
            if c.getSuit() != "heart":
                print("Player ",pNum," must spend the night in Jail")
                self.deck.discard(c)
                return False
            else:
                print("Player ",pNum," is released from Jail")
                self.deck.discard(c)
                return True
        return True

    #takes in a player number and checks if they have dynamite
    # returns true if they survive, false if they die
    def checkDynamite(self,pNum):
        if self.boards.hasDynamite(pNum):
            print("Player ",pNum," is holding Dynamite! Do not draw a 2-9 of spades!")
            c = self.deck.draw()
            print("Player ",pNum," drew a ",c.getNum()," of ",c.getSuit(),"s")
            if c.getSuit() == "spade" and c.getNum() >= 2 and c.getNum() <= 9:
                self.deck.discard(c)
                print("The Dynamite exploded! Player ",pNum," lost 3 health points!")
                for i in range(3):
                    if self.boards.decreaseHealth(pNum) == False:
                        print("Player ",pNum," has died!")
                        return False
                return True
            else:
                self.deck.discard(c)
                print("Player ",pNum," safely passed the Dynamite to the next player")
                self.boards.passDynamite(pNum)
                return True
        return True
            
    #asks if the user wants to play again
    def askPlayAgain(self):
        again = input("Do you want to play again (yes/no): ")
        while again != "yes" or again != "no":
            print("invalid input")
            again = input("Do you want to play again (yes/no): ")
        if again == 'yes':
            n = int(input("How many players (4-7): "))
            while n > 7 or n < 4:
                print("invalid input")
                n = int(input("How many players (4-7): "))
            self.playAgain(n)
            return
        elif again == "no":
            return
        return
                
    #takes in number of players and resets deck, players, and boards
    def PlayAgain(self,np):
        self.numPlayers = np
        deck = Deck()
        boards = BoardsBang(np)
        i = 0
        h = []
        while i < np:
            r = boards.getRole(i,True)
            h.append(deck.draw())
            h.append(deck.draw())
            h.append(deck.draw())
            h.append(deck.draw())
            if r == "Sheriff":
                h.append(deck.draw())
            p = PlayerBang(i,r,h)
            self.players.append(p)
            i = i+1
        self.played = False
        return




        