"""
This class is responsible for storing all the current information about the current state of the chess game.It will also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""

class gamestate():
    def __init__(self):
        #The board is an 8x8 #2D list and each element of the list has two characters, The first character represents the color of the piece(b or w) the second character represents the type of the piece(K-King,N-Knight and such).
        #The string "--" represents an empty space.
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteToMove = True
        self.movelog = []
    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move)  #log the move for later undo or to show the history
        self.whiteToMove = not self.whiteToMove   #swap the turns for the players

class move():

# Create mapping dictionary
    
    rows_to_ranks = {0:"8", 1:"7", 2:"6", 3:"5",
                 4:"4", 5:"3", 6:"2", 7:"1"}
    ranks_to_rows = {v:k for k,v in rows_to_ranks.items()}

    cols_to_files = {0:"a", 1:"b", 2:"c", 3:"d",
                 4:"e", 5:"f", 6:"g", 7:"h"}
    files_to_cols = {v:k for k,v in cols_to_files.items()}

    def __init__(self,startSq,endSq,board):
            self.startRow = startSq[0]
            self.startCol = startSq[1]
            self.endRow = endSq[0]
            self.endCol = endSq[1]
            self.pieceMoved = board[self.startRow][self.startCol]
            self.pieceCaptured = board[self.endRow][self.endCol]

    def get_chess_notation(self):
        #can be improved for better capture notation
        return self.get_rank_file(self.startRow,self.startCol) + self.get_rank_file(self.endRow,self.endCol)

    def get_rank_file(self,r,c):
        return self.cols_to_files[c] +  self.rows_to_ranks[r]
