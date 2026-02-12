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
