grid = ["#","#","#","#","#","#","#","#","#"]
# column-1 = [1,4,7] column-2 = [2,5,8] column-3 = [3,6,9]
# row-1 = [1,2,3] row-2 [4,5,6] row-3 = [7,8,9]
# wins = columns & rows & [1,5,9] [3,5,7]

def printer(matrix):
    i = 0
    while i < len(grid):
        print(matrix[i], end=" ")
        if i == 2 or i == 5 or i == 8:
            print("")
        i += 1
    user_input()

def unlooped_printer(matrix):
    i = 0
    while i < len(grid):
        print(matrix[i], end=" ")
        if i == 2 or i == 5 or i == 8:
            print("")
        i += 1

def user_input():
    valid_moves = ["1","2","3","4","5","6","7","8","9"]
    print("\nyour move: ", end="")
    uinp = input()
    if uinp in valid_moves:
        uinp = int(uinp)
        matrix_update(uinp)
    else:
        user_input()

def matrix_update(userinp):
    global grid
    grid[userinp-1] = "x"
    win_detect(grid)

def win_detect(matrix):
    columns = [
            [1,4,7],
            [2,5,8],
            [3,6,9],
            ]
    #
    rows = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
    #
    diagonals = [
        [1,5,9],
        [3,5,7],
        ]
    for i in range(0,3):
        if matrix[columns[i][0]-1] == "x" and matrix[columns[i][1]-1] == "x" and matrix[columns[i][2]-1] == "x":
            print('Player WIN!!!')
            unlooped_printer(matrix)
            return True
    for j in range(0,3):
        if matrix[rows[j][0]-1] == "x" and matrix[rows[j][1]-1] == "x" and matrix[rows[j][2]-1] == "x":
            print("Player WIN!!!")
            unlooped_printer(matrix)
            return True
    for d in range(0,2):
        if matrix[diagonals[d][0]-1] == "x" and matrix[diagonals[d][1]-1] == "x" and matrix[diagonals[d][2]-1] == "x":
            print("Player WIN!!!")
            unlooped_printer(matrix)
            return True
    aiwin(matrix)
    printer(matrix)

def aiwin(greid):
    for i in range(0,9):
        if greid[i] == "#":
            greid[i] = "o"
            work = visual_win(greid, "o")
            if work == True:
                unlooped_printer(greid)
                print("A.I Won :D")
                exit()
            elif work == False:
                greid[i] = "#"
    viwin(greid)

def viwin(greid):
    for i in range(0,9):
        if greid[i] == "#":
            greid[i] = "x"
            work = visual_win(greid, "x")
            if work == True:
                greid[i] = "o"
                unlooped_printer(greid)
                return
            elif work == False:
                greid[i] = "#"
    bestmove(greid)

def bestmove(greid):
    move = freecol(greid, "o")
    closed = 0
    if move != None:
        for i in range(0,3):
            if greid[move[i]-1] == "#":
                greid[move[i]-1] = "o"
                return
    for i in range(0,9):
        if greid[i] == "#":
            greid[i] = "o"
            unlooped_printer(greid)
            return
        else: closed += 1
        if closed >= 9:
            print("DRAW")
            exit()


def visual_win(matriex, sympol):
    columns = [
            [1,4,7],
            [2,5,8],
            [3,6,9],
            ]
    #
    rows = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
    #
    diagonals = [
        [1,5,9],
        [3,5,7],
        ]
    for i in range(0,3):
        if matriex[columns[i][0]-1] == sympol and matriex[columns[i][1]-1] == sympol and matriex[columns[i][2]-1] == sympol:
            return True
    for j in range(0,3):
        if matriex[rows[j][0]-1] == sympol and matriex[rows[j][1]-1] == sympol and matriex[rows[j][2]-1] == sympol:
            return True
    for d in range(0,2):
        if matriex[diagonals[d][0]-1] == sympol and matriex[diagonals[d][1]-1] == sympol and matriex[diagonals[d][2]-1] == sympol:
            return True
    return False

def freecol(matriex, sympol):
    columns = [
            [1,4,7],
            [2,5,8],
            [3,6,9],
            ]
    #
    rows = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
    #
    diagonals = [
        [1,5,9],
        [3,5,7],
        ]
    for i in range(0,3):
        if matriex[columns[i][0]-1] == sympol or matriex[columns[i][0]-1] == "#":
            if matriex[columns[i][1]-1] == sympol or matriex[columns[i][1]-1] == "#":
                if matriex[columns[i][2]-1] == sympol or matriex[columns[i][2]-1] == "#":
                    return columns[i]
    for j in range(0,3):
        if matriex[rows[j][0]-1] == sympol or matriex[rows[j][0]-1] == "#":
            if matriex[rows[j][1]-1] == sympol or matriex[rows[j][1]-1] == "#":
                if matriex[rows[j][2]-1] == sympol or matriex[rows[j][2]-1] == "#":
                    return rows[j]
    for d in range(0,2):
        if matriex[diagonals[d][0]-1] == sympol or matriex[diagonals[d][0]-1] == "#":
            if matriex[diagonals[d][1]-1] == sympol or matriex[diagonals[d][1]-1] == "#":
                if matriex[diagonals[d][2]-1] == sympol or matriex[diagonals[d][2]-1] == "#":
                    return diagonals[d]
    return None

printer(grid)
