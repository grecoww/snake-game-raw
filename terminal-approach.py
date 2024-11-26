import time
import os
import msvcrt
import random


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def killProcess(input):
    if input == 'q':
        exit()


def createBoard(rows, columns):
    matriz = []

    for _ in range(rows):
        newline = []
        matriz.append(newline)
        for _ in range(columns):
            newline.append('0')
    clearScreen()
    return matriz

#devem ter maneiras mais eficientes de renderizar o board (talvez usar buffers)
def showBoard(board):
    for i in range(len(board)):
        if i > 0:
            print()
        for j in board[i]:
            print(j, end='', flush=True)
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0


def createBody(board, coordinateArray, bodyCoord, initialize):
    coordinateArray.append([bodyCoord[0], bodyCoord[1]])
    if initialize:
        row = bodyCoord[0]
        column = bodyCoord[1]
        board[row][column]=1
    return coordinateArray



def createSugar(board):
    boardRows = len(board)
    boardColumns = len(board[0])

    row=random.randint(1, boardRows-2)
    column=random.randint(1, boardColumns-2)
    board[row][column]='*'
    return [row,column]


def moveBody(input, coordinatesArray):
    def moveHead(input, coordinatesArray):
        row = coordinatesArray[0][0]
        column = coordinatesArray[0][1]

        if not (row < 0 or column < 0 or row > boardRows-1 or column > boardColumns-1):

            if input == 'w':
                row-=1
            
            if input == 'a':
                column-=1
            
            if input == 's':
                row+=1
            
            if input == 'd':
                column+=1

            coordinatesArray[0] = [row, column]
            return coordinatesArray
        
        else: 

            killProcess('q')
    
    def moveTail(coordinatesArray):
        if len(coordinatesArray) > 1:
            for index in range(len(coordinatesArray)-1, 0, -1):
                coordinatesArray[index] = coordinatesArray[index-1]
            return coordinatesArray
        else:
            return coordinatesArray
        
    coordinatesArray = moveTail(coordinatesArray)
    coordinatesArray = moveHead(input, coordinatesArray)

    return coordinatesArray
        
            
def getTailCoord(coordinatesArray, input):
    if len(coordinatesArray) == 1:
        row = coordinatesArray[0][0]
        column = coordinatesArray[0][1]
    
        if input == 'w':
            row-=1
            return [row,column]
    
        if input == 'a':
            column-=1
            return [row,column]
    
        if input == 's':
            row+=1
            return [row,column]
    
        if input == 'd':
            column+=1
            return [row,column]

    else:
        tailCoord = coordinatesArray[-1]
        subTailCoord = coordinatesArray[-2]

        sumCoord = [subTailCoord[0]-tailCoord[0], subTailCoord[1]-tailCoord[1]]

        if sumCoord[0] == -1:
            return [tailCoord[0]-1, tailCoord[1]]
        
        if sumCoord[0] == 1:
            return [tailCoord[0]+1, tailCoord[1]]
        
        if sumCoord[1] == -1:
            return [tailCoord[0], tailCoord[1]+1]
        
        if sumCoord[1] == 1:
            return [tailCoord[0], tailCoord[1]-1]


def placeSugar(board, sugarCoord):
    board[sugarCoord[0]][sugarCoord[1]]='*'

def placePlayer(board, coordinatesArray):
    for coordinate in coordinatesArray:
        board[coordinate[0]][coordinate[1]]=1

def verifyCollision(coordinateArray):
    coordinateSet = set(tuple (coord) for coord in coordinateArray)
    if not len(coordinateSet) == len(coordinateArray):
        killProcess('q')

boardRows = 11
boardColumns = 21
running = True

row = int(boardRows/2)
column = int(boardColumns/2)

board = createBoard(boardRows, boardColumns)
coordinateArray = createBody(board, [], [row, column], initialize=True)
sugarCoord = createSugar(board)

while running:
    showBoard(board)
    direction = msvcrt.getwch()
    coordinateArray = createBody(board, coordinateArray, bodyCoord=getTailCoord(coordinateArray, direction), initialize=False)
    clearScreen()
    running2=True
    while running2:
        print(coordinateArray)
        if msvcrt.kbhit():
            direction = msvcrt.getwch()
        coordinateArray = moveBody(direction, coordinateArray)
        placePlayer(board, coordinateArray)
        verifyCollision(coordinateArray)
        if board[sugarCoord[0]][sugarCoord[1]] == 1:
            sugarCoord = createSugar(board)
            coordinateArray = createBody(board, coordinateArray, bodyCoord=getTailCoord(coordinateArray, direction), initialize=False)
        placeSugar(board, sugarCoord)
        showBoard(board)
        time.sleep(0.3)
        killProcess(direction) 
        clearScreen()
