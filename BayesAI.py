from bayespy.nodes import Categorical

class BayesAI:
    
    self.roles = ["Renegade","Outlaw","Deputy","Sherrif"]    
    
    def __init__(self, numPlayers, myRole, myPNum):
        self.players = []
        x = 0
        while x < numPlayers:
            if x == myPNum:
                self.players.append(0)
            else:
                self.players.append(self.playersNode(numPlayers, myRole))
        
    def playersNode(self, numPlayers, myRole):
        if numPlayers == 4:
            if myRole == self.roles[3]:
                p = [1/3,2/3]
            elif myRole == self.roles[0]:
                p = [0, 1]
            else:
                p = [1/2, 1/2]
                
        elif numPlayers == 5:
            if myRole == self.roles[3]:
                p = [1/4,1/2,1/4]
            elif myRole == self.roles[0]:
                p = [0,2/3,1/3]
            elif myRole == self.roles[1]:
                p = [1/3,1/3,1/3]
            else:
                p = [1/2,2/3,0]
       
       elif numPlayers == 6:
            if myRole == self.roles[3]:
                p = [1/5, 3/5, 1/5]
            elif myRole == self.roles[0]:
                p = [0, 3/4, 1/4]
            elif myRole == self.roles[2]:
                p = [1/4, 2/4, 1/4]
            else:
                p = [1/4, 3/4, 0]
        
        else:
            if myRole == self.roles[0]:
                p = [1/6, 3/6, 2/6]
            elif myRole == self.roles[1]:
                p = [0, 3/5, 2/5]
            elif myRole == self.roles[2]:
                p = [1/5, 2/5, 2/5]
            else:
                p = [1/5, 3/5, 1/5]
                
        return Categorical(p)
    
    def shotProbs(self,):
        