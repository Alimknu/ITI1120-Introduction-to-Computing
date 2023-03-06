def sumIntegers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def recursive_sumIntegers(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sumIntegers(n-1)

if sumIntegers(16) == recursive_sumIntegers(16):
    print("sumIntegers - Passed")
else:
    print("sumIntegers - Failed")

def sequence(n):
    seq = []
    while n!=1:
        seq.append(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
    seq.append(1)
    return seq

def recursive_sequence(n):
    x = 3#fix

if recursive_sequence(64) == sequence(64):
    print("sequence - Passed")
else:
    print("sequence - Failed")