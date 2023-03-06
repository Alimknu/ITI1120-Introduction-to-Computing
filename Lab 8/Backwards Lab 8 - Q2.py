#Backwards version of Lab 8 - Q2

def match_horizontal(puzzle, word, r, c):
    n = len(word)

    if c + 1 < n:
        return False

    for j in range(0, n):
        if word[j] != puzzle[r][c-j]:
            return False

    return True

def match_vertical(puzzle, word, r, c):
    n = len(word)

    if r + 1 < n:
        return False

    for j in range(0, n):
        if word[j] != puzzle[r-j][c]:
            return False

    return True

def match_diagonal(puzzle, word, r, c):
    n = len(word)

    if min(r+1, c+1) < n:
        return False

    for j in range(0,n):
        if word[j] != puzzle[r-j][c-j]:
            return False
    
    return True

def find_word(puzzle,  word):
    n = len(puzzle)

    for i in range(0,n):
        m = len(puzzle[0])
        for j in range(0, m):
            if match_horizontal(puzzle, word, i, j) or match_vertical(puzzle, word, i, j) or match_diagonal(puzzle, word, i, j):
                return i, j
    
    return -1, -1

n = int(input("Enter the number of rows: "))

puzzle = []

for i in range(0, n):
    print("Enter row number", i + 1,"of the puzzle: ", end = " ")
    row = input("")
    puzzle.append(row)

print("The puzzle:")
for i in range(0, n):
    print(puzzle[i])

word = input("Please enter the word to look for in the puzzle: ")

r, c = find_word(puzzle, word)

print(word, "is at row", r+1, "and columnn", c+1, end = ".")
