import time
import os
import msvcrt
import sys
import random


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


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

def createPlayer(board):
    row = int(len(board)/2)
    column = int(len(board[0])/2)
    board[row][column]=1
    return [row,column]

def movePlayer(board, input, coordinates):
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

    if input == 'q':
        sys.exit(0)

    return [row,column]

def createBody(board, input, coordinates):
    a=0

def moveBody(board, input, coordinates):
    a=0

def createSugar(board, boardRows, boardColumns):
    row=random.randint(1, boardRows)
    column=random.randint(1, boardColumns)
    board[row][column]=6
    return [row,column]


boardRows = 11
boardColumns = 21
running = True

board = createBoard(boardRows, boardColumns)
coord = createPlayer(board)
sugarCoord = createSugar(board, boardRows, boardColumns)

while running:
    showBoard(board)
    direction = msvcrt.getwch()
    clearScreen()
    running2=True
    while running2:
        showBoard(board)
        if board[sugarCoord[0]][sugarCoord[1]] == 0:
            sugarCoord = createSugar(board, boardRows, boardColumns)
        if msvcrt.kbhit():
            direction = msvcrt.getwch()
        lastDirection = direction
        coord = movePlayer(board, direction, coord)
        time.sleep(0.4)
        clearScreen()