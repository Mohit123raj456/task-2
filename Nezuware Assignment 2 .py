#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe 

# In[ ]:


#Import All required Modules

import pygame as pg

import sys

from pygame.locals import *

import numpy as np

# Initializing Pygame

pg.init()

# Pygame Screen

WIDTH=400

HEIGHT=400

# Colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GRAY = (200, 200, 200)

BLUE = (0, 0, 255)

#Tic Tac Toe Board

BOX_MARKED = (np.array([

    [0,0,0],

    [0,0,0],

    [0,0,0]

]))

#Other Global Variables

DRAW=False

WINNER=None

XO='o'

main_screen=pg.display.set_mode((WIDTH,HEIGHT+100))

pg.display.set_caption("Tic Tac Toe Game")

main_screen.fill(BLACK)



#Main Window and Grids

def starting_game():

    font=pg.font.Font(None,82)

    main_screen.fill(GRAY)

    text=font.render("Let's Play", True,BLUE,(GRAY))

    textRect = text.get_rect()

    textRect.center = (WIDTH // 2, HEIGHT // 2)

    main_screen.blit(text, textRect)

    pg.display.update()

    pg.time.wait(1200)

    main_screen.fill(WHITE)

    # Two Vertical lines

    pg.draw.line(main_screen,BLACK,(WIDTH/3,0),(WIDTH/3, HEIGHT),5)

    pg.draw.line(main_screen,BLACK,(WIDTH/3*2,0),(WIDTH/3*2, HEIGHT),5)

    # Two Horizontal lines

    pg.draw.line(main_screen,BLACK,(0,0),(WIDTH, 0),5)

    pg.draw.line(main_screen,BLACK,(0,HEIGHT/3),(WIDTH, HEIGHT/3),5)

    pg.draw.line(main_screen,BLACK,(0,HEIGHT/3*2),(WIDTH, HEIGHT/3*2),5)

    pg.draw.line(main_screen,BLACK,(0,HEIGHT),(WIDTH, HEIGHT),5)



#Getting Mouse x and y coordinates

def mouse_pointing():

    global row,col

    x, y = pg.mouse.get_pos()

    #  getting width of the box

    if(x<WIDTH/3) and (y<HEIGHT/3):

        row=0

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y<HEIGHT/3):

        row=0

        col=1

    elif(x>WIDTH/3*2) and (y<HEIGHT/3):

        row=0

        col=2

    elif(x<WIDTH/3) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=1

    elif(x>WIDTH/3*2) and (y>HEIGHT/3 and y<HEIGHT/3*2):

        row=1

        col=2

    elif(x<WIDTH/3) and (y>HEIGHT/3*2):

        row=2

        col=0

    elif(x>WIDTH/3 and x<WIDTH/3*2) and (y>HEIGHT/3*2):

        row=2

        col=1

    elif(x>WIDTH/3*2) and (y>HEIGHT/3*2):

        row=2

        col=2

    else:

        row=None

        col=None

    draw_figure(row,col)



#Drawing X and O on window

def draw_figure(row,col):

    global XO

    if(BOX_MARKED[row,col] == 0):

        global DRAW

        if row==0:

            posx = 65

        if row==1:

            posx = WIDTH/3 + 65

        if row==2:

            posx = WIDTH/3*2 + 65

        if col==0:

            posy = 65

        if col==1:

            posy = HEIGHT/3 + 65

        if col==2:

            posy = HEIGHT/3*2 + 65

        #Drawing X and O on mainscreen

        if(XO=='o'):

            pg.draw.circle(main_screen, BLACK, (posy, posx ), 40,8)

            BOX_MARKED[row][col] = 1

            XO='x'

        else:

            pg.draw.line (main_screen,BLACK, (posy - 30, posx - 30),

                         (posy + 30, posx + 30), 8)

            pg.draw.line (main_screen,BLACK, (posy + 30, posx - 30),

                         (posy - 30, posx + 30), 8)

            BOX_MARKED[row][col] = 2

            XO='o'

        pg.display.update()

        check_winner()

    else:

        pass

    #Show Player Message turns 

    message= XO.upper() + "'s Turn"

    font=pg.font.Font(None,70)

    text = font.render(message, True,BLUE,(WHITE))

    textRect = text.get_rect()

    textRect.center = (200,450)

    main_screen.blit(text, textRect)

    pg.display.update()



#This Function check winner and draw

def check_winner():

    global WINNER

    for row in range (0,3):

        if ((BOX_MARKED [row][0] == BOX_MARKED[row][1] == BOX_MARKED[row][2]) and(BOX_MARKED [row][0] != 0)):

            # this row won

            WINNER = BOX_MARKED[row][0]

            pg.draw.line(main_screen, BLACK, (0, (row + 1)*HEIGHT/3 -HEIGHT/6),\

                              (WIDTH, (row + 1)*HEIGHT/3 - HEIGHT/6 ), 4)

            show_winning_message(WINNER)

            break



    # check for winning columns

    for col in range (0, 3):

        if (BOX_MARKED[0][col] == BOX_MARKED[1][col] == BOX_MARKED[2][col]) and (BOX_MARKED[0][col] != 0):

            # this column won

            WINNER = BOX_MARKED[0][col]

            #draw winning line

            pg.draw.line (main_screen, BLACK,((col + 1)* WIDTH/3 - WIDTH/6, 0),\

                          ((col + 1)* WIDTH/3 - WIDTH/6, HEIGHT), 4)

            show_winning_message(WINNER)

            break



    # check for diagonal WINNERs

    if (BOX_MARKED[0][0] == BOX_MARKED[1][1] == BOX_MARKED[2][2]) and (BOX_MARKED[0][0] != 0):

        # game won diagonally left to right

        WINNER = BOX_MARKED[0][0]

        pg.draw.line (main_screen, BLACK, (50, 50), (350, 350), 4)

        show_winning_message(WINNER)

       



    if (BOX_MARKED[0][2] == BOX_MARKED[1][1] == BOX_MARKED[2][0]) and (BOX_MARKED[0][2] != 0):

        # game won diagonally right to left

        WINNER = BOX_MARKED[0][2]

        pg.draw.line (main_screen, BLACK, (350, 50), (50, 350), 4)

        show_winning_message(WINNER)

    

    if(all([all(row) for row in BOX_MARKED]) and WINNER is None ):

        DRAW = True

        show_winning_message('Match Draw')





def show_winning_message(winner):

    font=pg.font.Font(None,70)

    if winner == 1:

        winner = "O is winner "

    elif winner == 2:

        winner = "X is winner"

    else:

        pass

    text=font.render(winner, True,BLUE,(WHITE))

    textRect = text.get_rect()

    textRect.center = (200,450)

    main_screen.blit(text, textRect)

    

    pg.display.update()

    pg.time.wait(2000)

    reset_game()



def reset_game():

    global BOX_MARKED,DRAW,WINNER

    BOX_MARKED = (np.array([

        [0,0,0],

        [0,0,0],

        [0,0,0]

    ]))

    XO='x'

    DRAW=False

    WINNER=None

    starting_game()



starting_game()



#Program main loop

while(True):

    for event in pg.event.get():

        if event.type == QUIT:

            pg.quit()

            sys.exit()

        elif event.type==MOUSEBUTTONDOWN:

            mouse_pointing()

    pg.display.update()

    pg.display.flip()

