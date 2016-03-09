
def AlphaBetaAI:
    
    def __init__(self, players, myPNum, role):
        self.role = role
        self.numPlayers = players
        self.myPNum = myPNum
        
    #Choose the best move based on current board status
    def alphaBetaMove(self, board, ply):
        #variables are fun!        
        move = -1
        v = -INFINITY
        alpha = -INFINITY
        beta = INFINITY
        turn = self
        
        #Try shooting every player
        for p in range(self.numPlayers):
            if p != self.myPNum:
                if ply == 0:
                    return (self.score(board), p)

                if board.gameOver():
                    return (-1, -1)  # Can't make a move, the game is over
    
                newBoard = deepcopy(board)
                
                #Shoot player p
                newBoard.decreaseHealth(p)                
                
                #Next player
                nextPlayer = self.myPNum + 1
                if nextPlayer >= self.numPlayers:
                    nextPlayer -= self.numPlayers
                
                if not newBoard.showRole(nextPlayer, self.myPNum):
                    nextRole == 0
                else:
                    nextRole = newBoard.showRole(nextPlayer, self.myPNum)
                
                #Next player is created
                opp = AlphaBetaAI(self.numPlayers, nextPlayer, nextRole)
                
                #Next player goes
                s, oppMove = opp.minValueAB(newBoard, ply-1, turn, alpha, beta, self.myPNum-1)
    
                if s > v:
                    move = oppMove
                    v = s
                if v > alpha:
                    alpha = v
                if alpha >= beta:
                    break
        return (v, move)
    
    #Find the minimum value for the next move
    def maxValueAB( self, board, ply, turn, a, b):
        #If the game is over, stop
        if board.gameOver():
            return (turn.score(board), -1)

        #defining constants
        v = -INFINITY
        alpha = a
        move = -1

        #try shooting every player
       for p in range(self.numPlayers):
            if p != self.myPNum:
                #If you're at the end of your rope, stop
                if ply == 0:
                    return (self.score(board), p)

                #If check if the game is over
                if board.gameOver():
                    return (-1, -1)  
    
                #Copy the board
                newBoard = deepcopy(board)
                
                #Shoot player p
                newBoard.decreaseHealth(p)                
                
                #Next player
                nextPlayer = self.myPNum + 1
                if nextPlayer >= self.numPlayers:
                    nextPlayer -= self.numPlayers
                
                if not newBoard.showRole(nextPlayer, self.myPNum):
                    nextRole == 0
                else:
                    nextRole = newBoard.showRole(nextPlayer, self.myPNum)
                
                #Next player is created
                opp = AlphaBetaAI(self.numPlayers, nextPlayer, nextRole)
                
                #Next player goes
                s, oppMove = opp.minValueAB(nextBoard, ply-1, turn, a, b, self.numPlayers - 1)
    
                #Check your values
                if s > v:
                    move = oppMove
                    v = s
                if v > alpha:
                    alpha = v
                if b <= alpha:
                    break
        
        return (v, move)
    
    #Find the minimum value of the minimax alpha-beta pruning tree    
    def minValueAB(self, board, ply, turn, a, b, numMins):
       
       #If the game is over, stop
        if board.gameOver():
            return turn.score(board), -1

        #Defining numbers used        
        v = INFINITY
        beta = b
        move = -1

        #Try shooting every player
        for p in range(self.numPlayers):
            if p != self.myPNum:
                #If you're at the end of your rope, stop
                if ply == 0:
                    return (self.score(board), p)

                #If check if the game is over
                if board.gameOver():
                    return (-1, -1)  
    
                #Copy the board
                newBoard = deepcopy(board)
                
                #Shoot player p
                newBoard.decreaseHealth(p)                
                
                #Next player
                nextPlayer = self.myPNum + 1
                if nextPlayer >= self.numPlayers:
                    nextPlayer -= self.numPlayers
                
                if not newBoard.showRole(nextPlayer, self.myPNum):
                    nextRole == 0
                else:
                    nextRole = newBoard.showRole(nextPlayer, self.myPNum)
                
                #Next player is created
                opp = AlphaBetaAI(self.numPlayers, nextPlayer, nextRole)
                
                #Next player goes

                if numMins > 0:
                    s, oppMove = opp.minValueAB(nextBoard, ply-1, turn, a, b, numMins-1)
                else:
                    s, oppMove = opp.maxValueAB(nextBoard, ply-1, turn, a, b)
    

                if s < v:
                    v = s
                    move = oppMove
                if v < beta:
                    beta = v
                if beta <= a:
                    break
        
        return (v, move)

    #Scores the current set of players and health and returns a score based on your goals                
    def score(self, board):
        score = 0
        
        #Am I still alive?
        if board.getHealth(self.myPNum) > 0:
            score += 100
        else:
            score -= 100000000000000
        
        #Are people I want dead dead?
        if self.role == "Sheriff":
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum):
                        if board.showRole(p, self.myPNum) != "Deputy":
                            score += 100000
                        else:
                            score -= 10

        elif self.role == "Outlaw":
            if board.getSheriffHealth() == 0:
                score += 100000000
                for p in range(self.numPlayers):
                    if p != self.myPNum:
                        if board.showRole(p, self.myPNum):
                            score += 500
                        
        elif self.role == "Renegade":
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum) and board.showRole(p, self.myPNum) == "Outlaw" and board.getSheriffHealth() > 0:
                        score += 1000

        else: #Deputy
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum):
                        if board.showRole(p, self.myPNum) != "Sheriff" and board.getSheriffHealth() > 0:
                            score += 10000

        #Have I won?
        if board.winner() != None:
            if self.role in board.winner():
                score += 1000000000
            else:
                score -= 1000000000
        
        #How many people can I shoot?
        for p in range(self.numPlayers):
            if board.canShoot(self.myPNum,p,self.numPlayers):
                score += 50

        #Do I have good weapons to shoot people?
        if board.gunIsVolcanic(self.myPNum):
            score += 100
            
        #Bonuses for each good status effect
        for status in board.getStatus(self.myPNum):
            if status == "jail" or status == "dynamite":
                score -= 50
            else:
                score += 20
        
        #How many other people can shoot me?
        for p in range(self.numPlayers):
            if board.canShootMe(p,self.myPNum,numPlayers):
                if self.role == "Sheriff":
                    score -= 100
                else:
                    score -= 25
        
        #Number of people left to kill before I win:
        if self.role == "Sheriff":
            numOutlawsDead = 0            
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum):
                        if board.showRole(p, self.myPNum) == "Outlaw" or board.showRole(p, self.myPNum) == "Renegade":
                            numOutlawsDead += 1
            score -= 30*numOutlawsDead
        
        if self.role == "Deputy":
            numOutlawsDead = 0            
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum):
                        if board.showRole(p, self.myPNum) == "Outlaw" or board.showRole(p, self.myPNum) == "Renegade":
                            numOutlawsDead += 1
            score -= 30*numOutlawsDead

        if self.role == "Renegade":
            numPeopleDead = 0            
            for p in range(self.numPlayers):
                if p != self.myPNum:
                    if board.showRole(p, self.myPNum):
                        numPeopleDead += 1
            score -= 30*numPeopleDead
        
        #Return score
        return score