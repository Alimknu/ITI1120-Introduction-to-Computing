def ordered(a, e):
    order = False
    while order == False:
        for j in range(e):
            if (j+1 < e):
                if a[j] > a[j+1]:
                    temp = a[j+1]
                    a[j+1] = a[j]
                    a[j] = temp 
        for b in range(e):
            order = True
            if (b+1 < e):
                if a[b] > a[b+1]:
                    order = False
                    break
    return a

def average(a, e):
    value = 0
    for i in range(e):
        value = value + a[i]
    value = value/e
    print("Average = " + str(value))

def mode(a, e):
    for i in range(e):
        counter = 0
        for j in range(e):
            if a[j] == a[i]:
                counter = counter + 1
        if i == 0:
            arr = [counter]
        else:
            arr.append(counter)

    largest = arr[0]

    for i in range(e):
        if arr[i] > largest:
            largest = arr[i]

    modes = 0

    print("Mode(s) = ", end = "")
    for i in range(e):
        if largest == arr[i]:
            modes = modes + 1
            if modes % 2 == 0:
                if (modes/2 >= 2) and (modes/2 % 2 == 0):
                    print(",", end = " ")
                print(a[i], end = "")
    print()

def median(a, e):     
    if (e) % 2 == 0:
        med = (a[e//2] + a[(e//2)-1])/2
        print("Median = ", med)
    else:
        print("Median = " + str(a[(len(a)//2)]))

def scope(a, e):
    diff = a[e-1] - a[0]
    print("Range = " + str(diff))

n = int(input("Please enter the amount of numbers you wish to enter: "))

array = [8.910]

for x in range(n):
    num = float(input("Enter a number: "))
    if x == 0:
        array[0] = num
    else:
        array.append(num)

ordered(array, n)

average(array, n)
mode(array, n)
median(array, n)
scope(array, n)