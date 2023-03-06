def subString(s1, s2):
    found = False
    for i in range(len(s2)):
        for j in range(len(s2)+1):
            if s1 in s2[i:j]:
                found = True
                x = i
    if found == False:
        x = len(s2)

    return found, x
    

stringOne = input("Please enter a string: ")
stringTwo = input("Please enter another string: ")

a,b = subString(stringOne, stringTwo)

if (a == True):
    print(stringOne, "is a substring of", stringTwo)
    print("The last occurence of", stringOne, "is at index", b)

else:
    print(stringOne, "is not a substring of", stringTwo)
    print("The length of the second string is", b)