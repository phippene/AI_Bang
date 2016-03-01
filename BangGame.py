#Bang Game

import BoardsBang
import PlayerBang
import Deck

class BangGame:

    played = False
    NumPlayers = 0
    deck = None
    boards = None
    players = []

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
            while t != "human" || t != "ai":
                print("invalid input")
                t = input("What type of player is player",i," (human/ai): ")
            p = Player(i,r,h,t)
            players.append(p)
            i++

    #plays a game of Bang
    def Play(self):
        while played == False:
            played = True
            for player in players:
                if(boards.showRole(player.getPlayerNum(),True) == "Sheriff":
                   turn = player.getPlayerNum()
            while boards.winner() == None:
                if players[turn].getType() == "ai": #AI player
                   self.AITurn(turn)
                else: #human player
                    self.HumanTurn(turn)
                turn++
                if turn == numPlayers: #circle back
                   turn = 0
            print(boards.winner())
            self.askPlayAgain()
        return

    #plays an AI turn for player pNum
    def AITurn(self,pNum):
        return

    #plays a human turn for player pNum
    def HumanTurn(self,pNum):
        return

    #asks if the user wants to play again
    def askPlayAgain(self):
        again = input("Do you want to play again (yes/no): ")
        while again != "yes" || again != "no":
            print("invalid input")
            again = input("Do you want to play again (yes/no): ")
        if again == 'yes':
            n = input("How many players (4-7): ")
            while n > 7 || n < 4:
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
            i++
        played = False
        return




        
