import time
import os
import msvcrt
import sys
import random


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def killProcess(input):
    if input == 'q':
        sys.exit(0)


def createBoard(rows, columns):
    matriz = []

    for _ in range(rows):
        newline = []
        matriz.append(newline)
        for _ in range(columns):
            newline.append('0')
    clearScreen()
    return matriz


def showBoard(board):
    for i in range(len(board)):
        if i > 0:
            print()
        for j in board[i]:
            print(j, end='', flush=True)



def createBody(board, coordinates):
    row = coordinates[0]
    column = coordinates[1]

    board[row][column]=1

    return [row, column]


def createSugar(board, boardRows, boardColumns):
    row=random.randint(0, boardRows-1)
    column=random.randint(0, boardColumns-1)
    board[row][column]='*'
    return [row,column]



def moveHead(board, input, coordinates):
    row = coordinates[0]
    column = coordinates[1]

    if input == 'w':
        board[row][column]=0
        row-=1
        board[row][column]=1
        return [row,column]
    
    if input == 'a':
        board[row][column]=0
        column-=1
        board[row][column]=1
        return [row,column]
    
    if input == 's':
        board[row][column]=0
        row+=1
        board[row][column]=1
        return [row,column]
    
    if input == 'd':
        board[row][column]=0
        column+=1
        board[row][column]=1
        return [row,column]

    return [row,column]


def followHead(board, input, coordinates):
    row = coordinates[0]
    column = coordinates[1]

    board[row][column] = 1

    if input == 'w':
        board[row+1][column] = 0
    if input == 'a':
        board[row][column+1] = 0
    if input == 's':
        board[row-1][column] = 0
    if input == 'd':
        board[row][column-1] = 0


boardRows = 11
boardColumns = 21
running = True

row = int(boardRows/2)
column = int(boardColumns/2)

board = createBoard(boardRows, boardColumns)
coord = createBody(board, [row, column])
sugarCoord = createSugar(board, boardRows, boardColumns)
bodyCoord = None

while running:
    showBoard(board)
    direction = msvcrt.getwch()
    clearScreen()
    running2=True
    while running2:
        showBoard(board)
        if msvcrt.kbhit():
            direction = msvcrt.getwch()
        coord = moveHead(board, direction, coord)
        if board[sugarCoord[0]][sugarCoord[1]] == 0:
            bodyCoord = createBody(board, sugarCoord)
            sugarCoord = createSugar(board, boardRows, boardColumns)
        if bodyCoord != None:
            followHead(board, direction, bodyCoord)
            bodyCoord = coord
        time.sleep(0.4)
        killProcess(direction) 
        clearScreen()