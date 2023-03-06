stringOne = input("Please enter a string: ")
stringTwo = input("Please enter another string: ")

found = True

for x in range(len(stringOne)):
    if found == False:
        break
    found = False
    for i in range(len(stringOne)):
        if (i >= len(stringTwo)):
            found = False
            break
        if (stringOne[x] in stringTwo[i]):
            found = True

if (found == True):
    print("These strings are anagram.")
else:
    print("These strings are not anagram.")