stringOne = input("Please enter a string: ")
stringTwo = input("Please enter another string: ")

x = []

def inverse(s):
    rev = ""
    for i in range(0,len(s)):
        rev = rev + s[len(s)-1-i]
    return rev

stringTwo = inverse(stringTwo)

for i in range(len(stringTwo)):
    for j in range(len(stringTwo)+1):
        if stringOne == stringTwo[i:j]:
            if (-(len(stringTwo)-(i+1))) not in x:
                x.append(-(len(stringTwo)-(i+1)))
            temp = i
            i = i + j
            j = temp

stringTwo = inverse(stringTwo)

for i in range(len(stringTwo)+1):
    for j in range(len(stringTwo)+1):
        if stringOne == stringTwo[i:j]:
            if (j-len(stringOne)) not in x:
                x.append(j-len(stringOne))
            temp = i
            i = i + j
            j = temp

def ordered(a):
    e = len(a)
    order = False
    while order == False:
        for j in range(e):
            if (j+1 < e):
                if abs(a[j]) > abs(a[j+1]):
                    temp = a[j+1]
                    a[j+1] = a[j]
                    a[j] = temp 
        for b in range(e):
            order = True
            if (b+1 < e):
                if abs(a[b]) > abs(a[b+1]):
                    order = False
                    break
    return a

ordered(x)

print(x)