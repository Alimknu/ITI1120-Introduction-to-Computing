n = int(input("Please enter an integer: "))
b = int(input("Please enter the base you would like to convert to: "))

converted = [-2]

while n != 0:
    if (converted[0] == -2):
        converted[0] = (n%b)
    else:
        converted.append(n%b)
    n = n // b

for i in range(len(converted)):
    print(converted[-1-i], end = '')