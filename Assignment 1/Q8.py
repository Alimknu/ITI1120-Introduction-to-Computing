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

def setting(x, nX):
    for i in range(nX):
        element = int(input("Enter the element: "))
        if i == 0:
            x[0] = element
        else:
            x.append(element)
            
nU = int(input("How many elements are in the Universal set?: "))
u = [0]
setting(u, nU)

nA = int(input("How many elements are in the second set?: "))
a = [0]
setting(a, nA)

nB = int(input("How many elements are in the third set?: "))
b = [0]
setting(b, nB)

aUnionB = []
aPowerB = []

for i in range(nA):
    if a[i] not in aUnionB:
        aUnionB.append(a[i])
    if a[i] not in b and a[i] not in aPowerB:
        aPowerB.append(a[i])

for i in range(nB):
    if b[i] not in aUnionB:
        aUnionB.append(b[i])
    if b[i] not in a and b[i] not in aPowerB:
        aPowerB.append(b[i])

ordered(aUnionB, len(aUnionB))
ordered(aPowerB, len(aPowerB))

aIntersectionB = []

for i in range(nA):
    if a[i] in b and a[i] not in aIntersectionB:
        aIntersectionB.append(a[i])

ordered(aIntersectionB, len(aIntersectionB))

aMinusB = []

for i in range(nA):
    if a[i] not in b and a[i] not in aMinusB:
        aMinusB.append(a[i])

ordered(aMinusB, len(aMinusB))

bMinusA = []

for i in range(nB):
    if b[i] not in a and b[i] not in bMinusA:
        bMinusA.append(b[i])

ordered(bMinusA, len(bMinusA))

aComplement = []
bComplement = []

for i in range(nU):
    if u[i] not in a and u[i] not in aComplement:
        aComplement.append(u[i])
    if u[i] not in b and u[i] not in bComplement:
        bComplement.append(u[i])

ordered(aComplement, len(aComplement))
ordered(bComplement, len(bComplement))

print("A Union B = ", aUnionB)
print("A Intersection B = ", aIntersectionB)
print("A - B = ", aMinusB)
print("B - A = ", bMinusA)
print("A Complement = ", aComplement)
print("B Complement = ", bComplement)
print("A ^ B = ", aPowerB)