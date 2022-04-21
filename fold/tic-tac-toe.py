from turtle import bgcolor
import pygame,sys
import numpy as np

pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
RED=(255,0,0)
LINE_COL=(23,145,135)
LINE_WIDTH=15
BOARD_ROW=3
BOARD_COL=3
BG_color=(28,170,156)
screen.fill(BG_color)
#pygame.draw.line(screen,RED,(10,10),(300,300),10)
#drawing the board
board=np.zeros((BOARD_ROW,BOARD_COL))
#print(board)
def mark_square(row,col,player):
    board[row,col]=player
def avaliable_square(row,col):
    return board[row][col]==0
def is_board_full():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col]==0:
                return False
    return True

#main loop for the screen
def draw_line():
    #horizontal lines
    pygame.draw.line(screen,LINE_COL,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COL,(0,400),(600,400),LINE_WIDTH)
     #vertical lines
    pygame.draw.line(screen,LINE_COL,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COL,(400,0),(400,600),LINE_WIDTH)
     
draw_line()
while True:
    for event in pygame.event.get():
     if event.type==pygame.QUIT: 
       sys.exit()
    pygame.display.update()