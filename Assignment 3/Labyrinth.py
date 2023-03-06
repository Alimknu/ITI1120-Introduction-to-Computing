#Ali Mirzakhalili 300288698

def findEntrance(m): #looks for where the entrance is in the maze
    n = len(m)
    for row in range(n):
        if m[row][0] == 'p':
            return row

def move(m, r, c):#finds a move, it should also be a move that will have options after it is taken
    if m[r+1][c] == "p":
        if r+2 < len(m) and c+1 < len(m[0]):
            if m[r+1][c+1] == "p" or m[r+2][c] == "p" or m[r+1][c-1] == "p":
                r = r + 1
                return r, c, "↓"
        else:
            r = r + 1
            return r, c, "↓"

    elif m[r][c+1] == "p":
        if c+2 < len(m[0]) and r+1 < len(m):
            if m[r+1][c+1] == "p" or m[r][c+2] == "p" or m[r-1][c+1] == "p":
                c = c + 1
                return r, c, "→"
        else:
            c = c + 1
            return r,c, "→"

    elif m[r-1][c] == "p":
        if c+1 < len(m[0]) and r-2 > -1:
            if m[r-1][c+1] == "p" or m[r-2][c] == "p" or m[r-1][c-1] == "p":
                r = r - 1
                return r,c, "↑"
        else:
            r = r -1
            return r,c, "↑"

    elif m[r][c-1] == "p":
        if c-2 > -1 and r+1 < len(m):
            if m[r+1][c-1] == "p" or m[r][c-2] == "p" or m[r-1][c-1] == "p":
                c = c - 1
                return r,c, "↓"
        else:
            c = c - 1
            return r,c, "↓"

def solveLabyrinth(m):
    labyrinth = m #labyrinth[row][column]
    solution = False
    
    row = findEntrance(m) #the entrance
    column = 0
    exitColumn = len(m[0]) - 1#the exit's column
    symbol = "→"
    
    while solution == False:
        labyrinth[row][column] = symbol
        row, column, symbol = move(labyrinth, row, column)
        if column == exitColumn:
            labyrinth[row][column] = symbol
            solution = True
    return labyrinth

def solutionPrint(r):
    n = len(r)

    for i in range(n):
        for j in range(len(r[i])):
            print(r[i][j], end = " ")
        print()

#Main code
maze = []
i = 1

inputting = True
while inputting == True:
    ask = input("Enter row number " + str(i) + " of the maze: ")
    if not ask:
        inputting = False
        break
    ask = list(ask)
    maze.append(ask)
    i = i + 1

result = solveLabyrinth(maze)

solutionPrint(result)