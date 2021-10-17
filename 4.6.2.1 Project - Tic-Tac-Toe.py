import time # time.sleep(#)
from random import randrange
print("4.6.2.1 Project: Tic-Tac-Toe")

#########################################

def display_board(board):
    separator = str(("+"+"-"*7)*3+"+")
    spacer = str(("|"+" "*7)*3+"|")

    for row in board:
        beef = str("|   "+str(row[0])+"   |   "+str(row[1])+"   |   "+str(row[2])+"   |")
        print(separator)
        print(spacer)
        print(beef)
        print(spacer)
    #exit loop
    print(separator)
#exit function

#######################################

#### There is no check yet if the spot is taken

def enter_move(board01):
    spaces = make_list_of_free_fields(board01)
    #get a move from the person
    while True:
        move = int(input("Please enter a move: "))
        if move in spaces:
            break
        else:
            print("Input is not a valid space")
            time.sleep(1)

    #this bit puts the move in the board
    rownum = len(board01)
    for xxx in range(rownum): #gives list of [0,1,2]
        colnum = len(board01[xxx]) #length of board[0], board[1]...
        for yyy in range(colnum):
            if board[xxx][yyy] == move:
                board01[xxx][yyy] = "O"
            #exit if
        #exit for
    #exit for
    return board01
#exit function

#######################################

def make_list_of_free_fields(board):
    open_space = []
    for xx in range(3):
        for yy in range(3):
            if type(board[xx][yy]) == int:
                open_space.append(board[xx][yy])
        #exit for 1
    #exit for 2
    return open_space

#######################

def draw_move(board01):
    print("My turn...")
    time.sleep(1)
    
    spaces = make_list_of_free_fields(board01)
    comp_move = spaces[randrange(len(spaces))]

    rownum = len(board01)
    for xxx in range(rownum): #gives list of [0,1,2]
        colnum = len(board01[xxx]) #length of board[0], board[1]...
        for yyy in range(colnum):
            if board[xxx][yyy] == comp_move:
                board01[xxx][yyy] = "X"
            #exit if
        #exit for
    #exit for
    return board01
#exit function
    
#########################

def victory_for(board01):
    game_over = False
    empty_set = []
    if empty_set == make_list_of_free_fields(board01):
        return "Tie"
    for row in board01:
        if row[0]==row[1]==row[2]:
            game_over = True
    for cc in range(3):
        if board01[0][cc]==board01[1][cc]==board01[2][cc]:
            game_over = True
        #exit if
    #exit for loop
            
    if board01[1][1]==board01[0][0]==board01[2][2]:
        game_over = True
    if board01[1][1]==board01[0][2]==board01[2][0]:
        game_over = True
        
    return game_over
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game


################################
###############################

board=[[1,2,3],[4,5,6],[7,8,9]]
print(board)
#show board
display_board(board)

while True:
    #computer goes
    board = draw_move(board)
    display_board(board)

    #check win
    if victory_for(board) == "Tie":
        print("It is a tie...")
        break
    if victory_for(board):
        print("I win!")
        break
    #if no win, your turn
    board = enter_move(board)
    display_board(board)
    time.sleep(1)

    #check win
    if victory_for(board) == "Tie":
        print("It is a tie...")
        break
    if victory_for(board):
        print("You win!")
        break
    #If no wins, repeat...

time.sleep(3)
print("Good Bye...")
time.sleep(2)
