from BangGame import BangGame

class Tester:
    def runAI(self,numTrials,numPlayers):
        wins = [0,0,0,0] #Sheriff, Outlaws, Renegades, Deputies
        i = 0
        while i < numTrials:
            game = BangGame(numPlayers,"ai")
            result = game.Play()
            if "Sheriff" in result:
                wins[0] += 1
            elif "Outlaw" in result:
                wins[1] += 1
            elif "Renegade" in result:
                wins[2] += 1
            if "Deput" in result:
                wins[3] += 1

        print("Sheriff wins: ",wins[0]," Outlaw wins: ",wins[1])
        print("Renedage wins: ", wins[3]," Deputy wins: ",wins[3])
    
    def runDumbAI(self,numTrials,numPlayers):
        wins = [0,0,0,0] #Sheriff, Outlaws, Renegades, Deputies
        i = 0
        while i < numTrials:
            game = BangGame(numPlayers,"dumbAI")
            result = game.Play()
            if "Sheriff" in result:
                wins[0] += 1
            elif "Outlaw" in result:
                wins[1] += 1
            elif "Renegade" in result:
                wins[2] += 1
            if "Deput" in result:
                wins[3] += 1
            
        print("Sheriff wins: ",wins[0]," Outlaw wins: ",wins[1])
        print("Renedage wins: ", wins[3]," Deputy wins: ",wins[3])
    