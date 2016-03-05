#Bang Game

import BoardClass
import PlayerClass
import DeckClass

class BangGame:

    played = False
    NumPlayers = 0
    deck = None
    boards = None
    players = []
    guns = ["volcanic","schofield","remington","carabine","winchester"]
    meStatus = ["barrel","dynamite","mustang","scope"]

    #takes in number of players and sets up deck, players, and boards 
    def _init_(self, np):
        NumPlayers = np
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
            t = input("What type of player is player",i," (human/ai): ")
            while t != "human" or t != "ai":
                print("invalid input")
                t = input("What type of player is player",i," (human/ai): ")
            p = PlayerBang(i,r,h,t)
            players.append(p)
            i = i+1

    #plays a game of Bang
    def Play(self):
        while played == False:
            played = True
            for player in players:
                if boards.showRole(player.getPlayerNum(),True) == "Sheriff":
                   turn = player.getPlayerNum()
            while boards.winner() == None:
                if players[turn].getType() == "ai": #AI player
                   self.AITurn(turn)
                else: #human player
                    self.HumanTurn(turn)
                turn = turn+1
                if turn == numPlayers: #circle back
                   turn = 0
            print(boards.winner())
            self.askPlayAgain()
        return None

    #plays an AI turn for player pNum
    def AITurn(self,pNum):
        #check can play
        if boards.canPlay(pNum) == False:
            return None
        print("Player ",pNum,"'s Turn")
        #check dynamite
        if self.checkDynamite(pNum) == False:
            return None
        #check jail
        if self.checkJail(pNum) == False:
            return None
        #draw 2 cards
        startDraw(pNum)
        #play cards
        return None

    #plays a human turn for player pNum
    def HumanTurn(self,pNum):
        #check can play
        if boards.canPlay(pNum) == False:
            return None
        print("Player ",pNum,"'s Turn")
        #check dynamite
        if self.checkDynamite(pNum) == False:
            return None
        #check jail
        if self.checkJail(pNum) == False:
            return None
        #draw 2 cards
        startDraw(pNum)
        #play cards
        bang = False
        while players[pNum].handSize() > 0 and boards.canPlay(pNum):
            result = False
            while result == False:
                c = humanPickCard(pNum)
                result = humanPlayCard(pNum,c,bang)
        return None

    def humanPlayCard(self,pNum,c,bp):
        cname = c.getCard()
        if cname in guns:
            if boards.playGun(pNum,c) == False:
                print("error")
                return False
        elif cname in meStatus:
            if boards.playStatus(pNum,c) == False:
                print("you already have one of those")
                return False
        elif cname in guns:
            boards.playGun(pNum,c)
        elif cname == "bang":
            if bp == False or boards.gunIsVolcanic(pNum):
                if shootOne(pNum,c) == False:
                    return False
                return True
            print("You may use a Bang once per turn")
            return False
        elif cname == "duel":
            if duel(pNum,c) == False:
                return False
        elif cname == "panic":
            if panicCatBalou(pNum,True,c) == False:
                return False
        elif cname == "cat balou":
            if panicCatBalou(pNum,False,c) == False:
                return False
        elif cname == "jail":
            opp = input("which player would you like to put in jail: ")
            if boards.canJail(opp) == True:
                if boards.playStatus(opp,c) == False:
                   print("They are already in Jail")
        elif cname == "indians":
            shootAll(pNum,True)
        elif cname == "gatling":
            ShootAll(pNum,False)
        elif cname == "general store":
            generalStore(pNum)
        elif cname == "wells fargo":
            draw = [deck.draw(),deck.draw(),deck.draw()]
            players[pNum].addToHand(draw)
        elif cname == "stagecoach":
            draw = [deck.draw(),deck.draw()]
            players[pNum].addToHand(draw)
        elif cname == "beer":
            if boards.increaseHealth(pNum) == False:
                print("your health is already full")
                return False
        elif cname == "saloon":
            for i in range(numPlayers):
                boards.increaseHealth(pNum)
        elif cname == "missed":
            print("you cant play a 'missed' now")
            return False
        else:
            return False
        return True

    def duel(self,pNum,c):
        opp = input("who would you like to duel: ")
        while opp == pNum or opp >= numPlayers or opp < 0:
            print("Invalid player Number (enter -1 to retract card")
            opp = input("Please pick another Player: ")
            if opp == -1:
                return False
            deck.discard(c)
        again = False
        while again == False:
            if bangResponse(opp) == False:
                return True
            if bangResponse(pNum) == False:
                return True
        
    def panicCatBalou(self,pNum,panic,c):
        if panic:
            while cp == False:
                opp = input("Who would you like to panic: ")       
                while opp == pNum or opp >= numPlayers or opp < 0:
                    print("Invalid player Number (enter -1 to retract card")
                    opp = input("Please pick another Player: ")
                    if opp == -1:
                        return False
                cp = boards.canPanic(pNum,opp)
                if cp == False:
                    print("That player is out of range (enter -1 to retract card")
                    opp = input("Please pick another Player: ")
                    if opp == -1:
                        return False
            boards.displayBoard(opp)
            steal = input("which card would you like to steal: ")
            c2 = boards.removeStatus(opp,steal)
            if c2 == False:
                c2 = boards.removeGun(opp,steal)
                if c2 == False:
                    stealable = False
                else:
                    stealable = True
            while stealable == False:
                print("Invalid card (enter -1 to retract card)")
                steal = input("Please pick another card to steal: ")
                if steal == -1:
                    return False
                if steal != "colt.45":
                    stealable = True
                c2 = boards.removeStatus(opp,steal)
                if c2 == False:
                    c2 = boards.removeGun(opp,steal)
                    if c2 == False:
                        stealable = False
                    else:
                        stealable = True
            players[pNum].addToHand(c2)
            deck.discard(c)
            return True                        
        else:
            opp = input("Who would you like to cat balou: ")       
            while opp == pNum or opp >= numPlayers or opp < 0:
                print("Invalid player Number (enter -1 to retract card")
                opp = input("Please pick another Player: ")
                if opp == -1:
                    return False
            boards.displayBoard(opp)
            cb = input("which card would you like to cat balou: ")
            c2 = boards.removeStatus(opp,steal)
            if c2 == False:
                c2 = boards.removeGun(opp,steal)
                if c2 == False:
                    cbable = False
                else:
                    cbable = True
            while cbable == False:
                print("Invalid card (enter -1 to retract card")
                cb = input("Please pick another card to cat balou: ")
                if cb == -1:
                    return False
                if cb != "colt.45":
                    cbable = True
                c2 = boards.removeStatus(opp,steal)
                if c2 == False:
                    c2 = boards.removeGun(opp,steal)
                    if c2 == False:
                        cbable = False
                    else:
                        cbable = True 
            deck.discard(c)
            deck.discard(c2)
            return True
                      
    def generalStore(self,pNum,c):
        deck.discard(c)
        avail = []
        for i in range(NumPlayers):
            avail.append(deck.draw())
        circle = False
        start = pNum
        loc = pNum
        end = pNum-1
        if end < 0:
            end = NumPlayers-1
        while circle == False:
            i = 0
            for card in avail:
                print(i,": ",card.getCard())
                i = i+1
            c = input("which card would you like to take: ")
            while c not in range(avail.len()):
                print("invalid card")
                c = input("which card would you like to take: ")
            choice = avail[c]
            avail.remove(choice)
            players[loc].addToHand(choice)
            if loc != start:
                self.discardExtra(loc)
            loc = loc+1
            if loc == numPlayers:
                loc == 0
            if loc == start:
                circle = True
        return True
                    
            
    def disacardExtra(self,pNum):
        while players[pNum].handSize() > boards.checkHealth(pNum):
            c = self.humanPickCard(pNum)
            deck.discard(c)
        return True
            
    def missedResponse(self,oppNum):
        h = players[oppNum].rethand()
        for c in h:
            if c.getCard() == 'missed':
                use = input("would player",oppNum," like to play a missed (y/n): ")
                if use == "y":
                    deck.disacrd(c)
                    return True
                else:
                    boards.decreaseHealth(oppNum)
                    print("Player ",oppNum," was shot!")
                    return False
        return False
                         
    def bangResponse(self,oppNum):
        h = players[oppNum].rethand()
        for c in h:
            if c.getCard() == 'bang':
                use = input("would player",oppNum," like to play a Bang (y/n): ")
                if use == "y":
                    deck.disacrd(c)
                    return True
                else:
                    boards.decreaseHealth(oppNum)
                    print("Player ",oppNum," was shot!")
                    return False
        return False
                         
    def shootAll(self,pNum,indians,c):
        if indians:
            for p in range(numPlayers):
                if p != pNum:
                    bangResponse()
        else:
            for p in range(numPlayers):
                if p != pNum:
                    missedResponse()
        deck.discard(c)
        return True
                         
    def shootOne(self,pNum,c):
        opp = input("Who would you like to shoot: ")
        cs = False
        while cs == False:
            while opp == pNum or opp >= numPlayers or opp < 0:
                print("Invalid player Number (enter -1 to retract card)")
                opp = input("Please pick another Player: ")
                if opp == -1:
                    return False
            cs = boards.canShoot(pNum,opp)
            if cs == False:
                print("That player is out of range (enter -1 to retract card)")
                opp = input("Please pick another Player: ")
                if opp == -1:
                    return False
        missedResponse(opp)
        deck.discard(c)
        return True
                                    
    def humanPickCard(self,pNum):
        players[pNum].displayHand()
        cnum = input("Which card would you like to play: ")
        c = players[pNum].getFromHand(cnum)
        return c

    #takes in player number and draws two cards
    def startDraw(self,pNum):
        c = [deck.draw(), deck.draw()]
        players[pNum].addToHand(c)
        return None
        
    #takes in player number and checks if they are in jail
    #returns true if they get out and false if they are suck
    def checkJail(self,pNum):
        if boards.inJail(pNum):
            print("Player ",pNum," is in Jail and must draw a heart to play!")
            c = deck.draw()
            print("Player ",pNum," drew a ",c.getSuit())
            if c.getSuit() != "heart":
                print("Player ",pNum," must spend the night in Jail")
                deck.discard(c)
                return False
            else:
                print("Player ",pNum," is released from Jail")
                deck.discard(c)
                return True
        return True

    #takes in a player number and checks if they have dynamite
    # returns true if they survive, false if they die
    def checkDynamite(self,pNum):
        if boards.hasDynamite(pNum):
            print("Player ",pNum," is holding Dynamite! Do not draw a 2-9 of spades!")
            c = deck.draw()
            print("Player ",pNum," drew a ",c.getNum()," of ",c.getSuit(),"s")
            if c.getSuit() == "spade" and c.getNum() >= 2 and c.getNum() <= 9:
                deck.discard(c)
                print("The Dynamite exploded! Player ",pNum," lost 3 health points!")
                for i in range(3):
                    if boards.decreaseHealth(pNum) == False:
                        print("Player ",pNum," has died!")
                        return False
                return True
            else:
                deck.discard(c)
                print("Player ",pNum," safely passed the Dynamite to the next player")
                boards.passDynamite(pNum)
                return True
        return True
            
    #asks if the user wants to play again
    def askPlayAgain(self):
        again = input("Do you want to play again (yes/no): ")
        while again != "yes" or again != "no":
            print("invalid input")
            again = input("Do you want to play again (yes/no): ")
        if again == 'yes':
            n = input("How many players (4-7): ")
            while n > 7 or n < 4:
                print("invalid input")
                n = input("How many players (4-7): ")
            self.playAgain(n)
            return
        elif again == "no":
            return
        return
                
    #takes in number of players and resets deck, players, and boards
    def PlayAgain(self,np):
        NumPlayers = np
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
            p = Player(i,r,h)
            players.append(p)
            i = i+1
        played = False
        return




        
