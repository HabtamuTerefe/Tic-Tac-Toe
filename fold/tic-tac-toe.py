from turtle import bgcolor
import pygame,sys
import numpy as np

pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(" Tic Tac Toe")
RED=(255,0,0)
LINE_COL=(23,145,135)
LINE_WIDTH=15
circle_radius=60
circle_width=15
cross_width=25
cross_space=55
BOARD_ROW=3
BOARD_COL=3
circle_col=(239,231,200)
cross_col=(66,66,66)
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
def check_win(player):
    #vertical win check
    for col in range(BOARD_COL):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
           vertical_wining_line(col,player)
           return True
    #horizontal win check
    for row in range(BOARD_ROW):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            horizontal_wining_line(row,player)
            return True
    #asc win check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        asc_diagonal(player)
        return True
    #dsc win check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        dsc_diagonal(player)
        return True
    return False


def vertical_wining_line(col,player):
    pos_x=col*200+100
    if player==1:
        color=circle_col
    elif player==2:
        color=cross_col
    pygame.draw.line(screen,color,(pos_x,15),(pos_x,HEIGHT-15),15)
  
def horizontal_wining_line(row,player):
     pos_y=row*200+100
     if player==1:
        color=circle_col
     elif player==2:
        color=cross_col
     pygame.draw.line(screen,color,(15,pos_y),(WIDTH-15,pos_y),15)
def asc_diagonal(player):
     if player==1:
        color=circle_col
     elif player==2:
        color=cross_col
     pygame.draw.line(screen,color,(15,HEIGHT-15,),(WIDTH-15,15),15)
def dsc_diagonal(player):
    if player==1:
        color=circle_col
    elif player==2:
        color=cross_col
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)
    



#main loop for the screen
def draw_line():
    #horizontal lines
    pygame.draw.line(screen,LINE_COL,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COL,(0,400),(600,400),LINE_WIDTH)
     #vertical lines
    pygame.draw.line(screen,LINE_COL,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COL,(400,0),(400,600),LINE_WIDTH)
draw_line()
def draw_figures():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col]==1:
              pygame.draw.circle(screen,circle_col,(int(col*200+100),int(row*200+100)),circle_radius,circle_width)
            elif board[row][col]==2:
                pygame.draw.line(screen,cross_col,(col*200+cross_space,row*200+200-cross_space),(col*200+200-cross_space,row*200+cross_space),cross_width)
                pygame.draw.line(screen,cross_col,(col*200+cross_space,row*200+cross_space),(col*200+200-cross_space,row*200+200-cross_space),cross_width)
def restart():
    screen.fill(bgcolor)
    draw_line()
    player=1
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col]=0



     

player=1
game_over=False
while True:
    for event in pygame.event.get():
     if event.type==pygame.QUIT: 
       sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
        mouse_x=event.pos[0]
        mouse_y=event.pos[1]
        clicked_row=int(mouse_y // 200)
        clicked_col=int(mouse_x // 200)
        
        if avaliable_square(clicked_row,clicked_col):
            if player==1:
               mark_square(clicked_row,clicked_col,1)
               if  check_win(player):
                  game_over=True
               player=2
            elif player==2:
                mark_square(clicked_row,clicked_col,2)
                if  check_win(player):
                  game_over=True
                player=1
            draw_figures()
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_r:
            restart()



    
    pygame.display.update()