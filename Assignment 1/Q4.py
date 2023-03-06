n = int(input("How many lines of Pascal's triangle?: "))

def factorial(x):
    f = 1
    for i in range(2,x+1):
        f = f*i
    return f

for i in range(n):
    for j in range(i):
        value = factorial(i)/(factorial(j)*(factorial(i-j)))
        print(int(value), end = ' ')
    print("1")