
import numpy as np
import random
import math

# self class is responsible for representing the game board
class GenGameBoard: 
    
    # Constructor method - initializes each position variable and the board size
    def __init__(self, boardSize):
        self.boardSize = boardSize  # Holds the size of the board
        self.marks = np.empty((boardSize, boardSize),dtype='str')  # Holds the mark for each position
        self.marks[:,:] = ' '
    
    # Prints the game board using current marks
    def printBoard(self): 
        # Prthe column numbers
        print(' ',end='')
        for j in range(self.boardSize):
            print(" "+str(j+1), end='')
        
        
        # Prthe rows with marks
        print("")
        for i in range(self.boardSize):
            # Prthe line separating the row
            print(" ",end='')
            for j in range(self.boardSize):
                print("--",end='')
            
            print("-")

            # Prthe row number
            print(i+1,end='')
            
            # Prthe marks on self row
            for j in range(self.boardSize):
                print("|"+self.marks[i][j],end='')
            
            print("|")
                
        
        # Prthe line separating the last row
        print(" ",end='')
        for j in range(self.boardSize):
            print("--",end='')
        
        print("-")
    
    
    # Attempts to make a move given the row,col and mark
    # If move cannot be made, returns False and prints a message if mark is 'X'
    # Otherwise, returns True
    def makeMove(self, row, col, mark):
        possible = False  # Variable to hold the return value
        if row==-1 and col==-1:
            return False
        
        # Change the row,col entries to array indexes
        row = row - 1
        col = col - 1
        
        if row<0 or row>=self.boardSize or col<0 or col>=self.boardSize:
            print("Not a valid row or column!")
            return False
        
        # Check row and col, and make sure space is empty
        # If empty, set the position to the mark and change possible to True
        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    
        
        # Prout the message to the player if the move was not possible
        if not possible and mark=='X':
            print("\nself position is already taken!")
        
        return possible
    
    
    # Determines whether a game winning condition exists
    # If so, returns True, and False otherwise
    def checkWin(self, mark):
        won = False # Variable holding the return value
        
        # Check wins by examining each combination of positions
        
        # Check each row
        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break
        
        # Check each column
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break

        # Check first diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        # Check second diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won
    
    # Determines whether the board is full
    # If full, returns True, and False otherwise
    def noMoreMoves(self):
        return (self.marks!=' ').all()


    def makeCompMove(self):
        maxx, maxy = -1, -1
        (m, x, y) = self.max_alpha_beta(-2,2)
        # print("x equals " + str(px)) Debugging purposes only
        # print("y equals " + str(py)) Debugging purposes only
        self.makeMove(x+1,y+1,'O') # Make move, add 1 to each variable for array purposes
        print("Computer chose: "+str(x+1)+","+str(y+1)) # Print result, adjusting for array again
        
        # Run alpha beta search here

    def max_alpha_beta(self, alpha, beta): # Optimal/Max score for AI
        maxalpha = -2 # Worst case alpha for AI
        maxx = None
        maxy = None

        # Establish whether or not the game is still in play for algorithm
        if board.checkWin('X'): #Check to see if AI lost
            return (-1, 0, 0)
        elif board.checkWin('O'): # Check to see if AI won
            return (1, 0, 0)
        elif board.noMoreMoves(): # Check to see if draw
            return (0, 0, 0)

        for s in range(0, self.boardSize-1):
            for t in range(0, self.boardSize-1):
                if self.marks[s][t] == ' ':
                    self.marks[s][t] = 'O' #Attempt first open slot and check max
                    (m, max_s, max_t) = self.min_alpha_beta(alpha, beta)
                    if m > maxalpha:
                        maxalpha = m
                        maxx = s
                        maxy = t
                    self.marks[s][t] = ' ' # reset the mark

                    ## Alpha Beta Pruning
                    if maxalpha >= beta:
                        return (maxalpha, maxx, maxy)

                    if maxalpha > alpha:
                        alpha = maxalpha

        return (maxalpha, maxx, maxy)

    def min_alpha_beta(self, alpha, beta): #Optimal/Max score for player
        minalpha = 2 # Worst case for player
        minx = None
        miny = None

        # Establish whether or not the game is still in play for algorithm
        if board.checkWin('X'): # Check to see if AI lost
            return (-1, 0, 0)
        elif board.checkWin('O'): # Check to see if AI won
            return (1, 0, 0)
        elif board.noMoreMoves(): # check for Draw
            return (0, 0, 0)

        for s in range(0, self.boardSize-1):
            for t in range(0, self.boardSize-1):
                if self.marks[s][t] == ' ':
                    self.marks[s][t] = 'X' #Attempt first open slot and check max
                    (m, min_s, min_t) = self.max_alpha_beta(alpha, beta) #
                    if m < minalpha:
                        minalpha = m
                        minx = s
                        miny = t
                    self.marks[s][t] = ' ' # reset the mark

                    ## Alpha Beta Pruning
                    if minalpha <= alpha:
                        return (minalpha, minx, miny)

                    if minalpha < beta:
                        beta = minalpha

        return (minalpha, minx, miny)


print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Scott Carrington")

LOST = 0
WON = 1
DRAW = 2    
wrongInput = False
boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        
# Create the game board of the given size
board = GenGameBoard(boardSize)
        
board.printBoard()  # Print the board before starting the game loop
        
# Game loop
while True:
    # *** Player's move ***        
    
    # Try to make the move and check if it was possible
    # If not possible get col,row inputs from player    
    row, col = -1, -1
    while not board.makeMove(row, col, 'X'):
        print("Player's Move")
        row, col = input("Choose your move (row, column): ").split(',')
        row = int(row)
        col = int(col)

    # Display the board again
    board.printBoard()
            
    # Check for ending condition
    # If game is over, check if player won and end the game
    if board.checkWin('X'):
        # Player won
        result = WON
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
            
    # *** Computer's move ***
    board.makeCompMove()
    
    # Print out the board again
    board.printBoard()    
    
    # Check for ending condition
    # If game is over, check if computer won and end the game
    if board.checkWin('O'):
        # Computer won
        result = LOST
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
        
# Check the game result and print out the appropriate message
print("GAME OVER")
if result==WON:
    print("You Won!")            
elif result==LOST:
    print("You Lost!")
else: 
    print("It was a draw!")

