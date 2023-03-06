import math #This code is horribly wrong

n = int(input("Please enter the number of rows: "))
m = int(input("Please enter the number of columns: "))

rectangles = 0
squares = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        rectangles = rectangles + 1
        if (math.sqrt(i*j) == i):#don't know how else to tell if there's a square
            squares = squares + 1

notSquares = rectangles - squares

print("Total number of rectangles = ", rectangles)
print("Rectangles but not squares = ", notSquares)