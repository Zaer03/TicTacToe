import time
import random
import os #was going to have this to clear the terminal
class TicTacToe():
    def __init__(self):
        self.board = []
        
    def makeBoard(self):
        self.board = []
        global board
        board = [[7,8,9], [4,5,6], [1,2,3]]
        for i in range(0, 3):
            print(*board[i], sep=' | ')
            if i != 2:
                print("- + - + -")
            else:
                break
            
    def turnRNG(self):
        return random.randint(0, 1) #randomly selects every time it loops, maybe move it outside the function and reference it?
    
    def wincon(self, player):
        for i in range(3): #### horizontal checks ####
            for j in range(3):
                x = all(elem == board[i][j] for elem in board[i])
                if x == True and board[i][0] == player:
                    return True
        vcount = 0
        for i in range(3): #### vertical checks ####
            for j in range(3):
                if board[j][i] == player: 
                #can't do the all() function because it returns a "None" value at the end of a list
                    vcount += 1
                if vcount < 3 and j == 2:
                    vcount = 0
                elif vcount == 3 and j == 2:
                    return True
        d1count = 0 # one diagonal
        d2count = 0 # the other diagonal
        for i in range(3):
            if board[i][i] == player:
                d1count += 1
            if d1count == 3 and i == 2:
                return True
            if board[i][2-i] == player:
                d2count += 1
            if d2count == 3 and i == 2:
                return True
        return False
        
    def isBoardFull(self):
        intCount = 9
        for i in range(3):
            for ele in board[i]:
                if(type(ele) == str):
                    intCount -= 1
        if intCount == 0:
            return True 
        else:
            return False
            
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
        
    def refreshBoard(self):
        for i in range(0, 3):
            print(*board[i], sep=' | ')
            if i != 2:
                print("- + - + -")
            else:
                break
            
    def start(self):
        os.system('cls||clear')
        self.makeBoard()
        player = 'X' if self.turnRNG() == 1 else 'O'
        while True:
        
            print(f"Player {player} turn")
            
            turn = int(input())
            if isinstance(turn, int) == True:
                if turn == 7 and isinstance(board[0][0], int) == True:
                    board[0][0] = player
                elif turn == 8 and isinstance(board[0][1], int) == True:
                    board[0][1] = player
                elif turn == 9 and isinstance(board[0][2], int) == True:
                    board[0][2] = player
                elif turn == 4 and isinstance(board[1][0], int) == True:
                    board[1][0] = player
                elif turn == 5 and isinstance(board[1][1], int) == True:
                    board[1][1] = player
                elif turn == 6 and isinstance(board[1][2], int) == True:
                    board[1][2] = player
                elif turn == 1 and isinstance(board[2][0], int) == True:
                    board[2][0] = player
                elif turn == 2 and isinstance(board[2][1], int) == True:
                    board[2][1] = player
                elif turn == 3 and isinstance(board[2][2], int) == True:
                    board[2][2] = player
            else:
                print("Not a valid position! Please reenter your move")
                 
            # checking whether current player is won or not
            if self.wincon(player):
                os.system('cls||clear')
                self.refreshBoard()
                print(f"Player {player} wins the game!")
                break

            # If board is full and no wincon has been met, declares draw        
            if self.isBoardFull():
                os.system('cls||clear')
                self.refreshBoard() 
                print("Match Draw!")
                break
            # Switch turns
            player = self.swap_player_turn(player)

            # Clear terminal, refreshes board so you don't have to scroll as the game progresses
            os.system('cls||clear')
            self.refreshBoard()

        ### Fix reset loop ###
        '''print("Would you like to play again? y/n")
        newGameConfirm = str(input())
        if newGameConfirm == 'y':
            print("New game coming right up!")
            time.sleep(1)
            #return True
            break
        elif newGameConfirm == 'n':
            print("Thanks for playing!")
            time.sleep(1)
            break #return False
        else:
            print('entered input was invalid, exiting game')
            time.sleep(1)
            break '''

tic_tac_toe = TicTacToe()
tic_tac_toe.start()

#DONE    ### find a way to prevent overwriting ###  
### find a way to not switch players if other player had invalid input ###

