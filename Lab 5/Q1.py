
from re import I


def sumOfFactors(n):
    value = 0
    array = [0]
    counter = 0
    for i in range(1, n):
        if (n % i == 0):
            if (counter == 0):
                array[counter] = i
            else:
                array.append(i)
            counter = counter + 1

    for x in range(counter):
        value = value + array[x]

    return value

n = int(input("Please enter the number: "))

result = sumOfFactors(n)

if result != n:
    print(n, "is not a complete number.")
else:
    print(n, "is a complete number.")