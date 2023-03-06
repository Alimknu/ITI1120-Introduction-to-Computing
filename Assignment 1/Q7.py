from this import d


matrix = [0.0, 0.0, 0.0, 0.0][0.0, 0.0, 0.0, 0.0][0.0, 0.0, 0.0, 0.0]#refer to Cramer's rule as u code

for i in range(3):
    for j in range(4):
        ask = float(input("Enter the coefficient: "))
        matrix[i][j] = ask

#find determinants:
#I couldn't figure out how to find the determinants, I read the Cramer's rule many times over and still didn't get it

if (d == 0):#if the determinant in the end is 0
    if (dX == 0 and dY == 0 and dZ == 0):#if all determinants are 0
        print("There are an infinite number of answers!")
    else:#if one of the determinants are not zero
        print("No answer found!")

else:#for when there's one solution
    x = dX/d
    y = dY/d
    z = dZ/d

    print("x = ", x)
    print("y = ", y)
    print("z = ", z)