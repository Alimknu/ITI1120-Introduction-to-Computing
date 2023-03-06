from json.encoder import INFINITY


n = int(input("Please enter a positive integer greater than 1: "))

numList = [8.910]

for g in range(n):
    a = float(input("Please enter a number: "))
    if (g == 0):
        numList[0] = a
    else:
        numList.append(a)

minDiff = INFINITY
x = INFINITY
y = INFINITY

for i in range(n-1):
    for j in range(i+1,n):
        if (abs(numList[i] - numList[j]) < minDiff):
            minDiff = abs(numList[i] - numList[j])
            if (numList[i] < numList[j]):
                x = numList[i]
                y = numList[j]
            else:
                x = numList[j]
                y = numList[i]
        elif(abs(numList[i] - numList[j]) == minDiff):
            if (numList[i] < numList[j]):
                if (numList[i] < x):
                    x = numList[i]
                    y = numList[j]
            else:
                if (numList[j] < x):
                    x = numList[j]
                    y = numList[i]

print(x,y)