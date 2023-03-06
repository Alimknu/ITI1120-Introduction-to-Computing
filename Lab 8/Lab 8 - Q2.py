def match_horizontal(puzzle, word, r, c):
    n = len(word)

    if c + 1 > n:
        return False

    for j in range(0, n):
        if word[j] != puzzle[r][c+j]:
            return False

    return True

def match_vertical(puzzle, word, r, c):
    n = len(word)

    if r + 1 > n:
        return False

    for j in range(0, n):
        if word[j] != puzzle[r+j][c]:
            return False

    return True

def match_diagonal(puzzle, word, r, c):
    n = len(word)

    if max(r+1, c+1) >= n:
        return False

    for j in range(0,n):
        if word[j] != puzzle[r+j][c+j]:
            return False
    
    return True

def find_word(puzzle, word):
    n = len(puzzle)
    h = False
    v = False
    d = False

    for i in range(0, n):
        m = len(puzzle[0])
        for j in range(0, m):
            if match_horizontal(puzzle, word, i, j):
                h = True
                return i,j, h, v, d
            elif match_vertical(puzzle, word, i, j): 
                v = True
                return i,j, h, v, d

            elif match_diagonal(puzzle, word, i, j):
                d = True
                return i,j, h, v, d
    
    return -1, -1, h, v, d

n = int(input("Enter the number of rows: "))

puzzle = []
horizontal = False
vertical = False
diagonal = False

for i in range(0, n):
    print("Enter row number", i + 1,"of the puzzle: ", end = " ")
    row = input("")
    puzzle.append(row)

print("The puzzle:")
for i in range(0, n):
    print(puzzle[i])

word = input("Please enter the word to look for in the puzzle: ")

r, c, horizontal, vertical, diagonal = find_word(puzzle, word)

if horizontal == True or vertical == True or diagonal == True:
    print(word, "is found at row", r+1, "and columnn", c+1, end = " ")

else:
    print(word, "is not found within the puzzle.")

if horizontal == True:
    print("horizontally.")
elif vertical == True:
    print("vertically.")
elif diagonal == True:
    print("diagonally.")

