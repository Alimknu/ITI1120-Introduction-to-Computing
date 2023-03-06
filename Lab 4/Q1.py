n = int(input("Please enter a positive integer greater than 2: "))

list = []

for x in range(n):
    a = int(input("Input an integer: "))
    list.append(a)

unique = 0

for i in range(n):
    temp = list[i]
    if (i+1 >= n):
        list[i] = list[i-1]
    else:
        list[i] = list[i+1]
    if (temp in list):
        list[i] = temp
        continue
    else:
        unique = temp
        break

print("The unique number = ", unique)