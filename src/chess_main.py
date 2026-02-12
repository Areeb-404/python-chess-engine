"""
This is our main driver file. It will be responsible for handling user input and displaying the current Gamestate Object.
"""

import pygame as p
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8 #DIMENSION of a chess board is 8x8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Load Images will initialize a global dictionary of images. This will be called exactly once in main.
"""

def load_Images():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("assets/"+piece+".png"),(SQ_SIZE,SQ_SIZE))
    #Note: We can access an image by using a dictionary like IMAGES['wp'] as it exists as wp in the dictionary

    """
    This will be the main driver for the code. This will handle user input and updating the graphics
    """

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.gamestate()  #Initializes the constructor and hence the gamestate
    load_Images() #only done once hence before the while loop

    running = True
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running = False

        draw_game_state(screen,gs)
        clock.tick((MAX_FPS))   #type:ignore
        p.display.flip() #flips the board for the other side's turn

# draw_game_state - responsible for all the graphics in current game state

def draw_game_state(screen,gs):
    drawboard(screen)  #Draws the squares on the board
    drawpieces(screen,gs.board) #Draws the pieces on top of the square created by the drawboard function

def drawboard(screen):
    #NOTE : In chess the top left square is always white.
    colors = [p.Color("#769656"),p.Color("#eeeed2")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            #using color parity characteristic of a chess board(google chess board color parity condition if dont know)
            color = colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def drawpieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece!="--":    #if the square is not empty
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

main()
