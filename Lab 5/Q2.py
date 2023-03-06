import math

def average(num, numarray):
    value = 0
    for i in range(num):
        value = value + numarray[i]
    value = value / num

    return value

def sDev(num, numarray, ave):
    sumSquared = 0
    for i in range(num):
        sumSquared = sumSquared + (numarray[i] - ave)**2
    deviation = (sumSquared/(num))**0.5
    return deviation

n = int(input("Please enter the amount of numbers: "))
array = [8.910]
for i in range(n):
    x = float(input("Enter a number: "))
    if (i == 0):
        array[0] = x
    else:
        array.append(x)

avg = average(n, array)
standardDeviation = sDev(n, array, avg)

print("The standard deviation is", standardDeviation)