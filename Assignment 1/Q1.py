n = int(input("Enter an integer: "))

print(n, end = " = ")#start the output of the code
counter = 1#establish this counter for knowing the powers of a number(starts at 1 so it follows exponents properly, every integer has the default exponent of 1)
original = n#remembers the original value

prime = True

for i in range(2, (original//2)+1):#starts at 2 because we don't include 1
    if (n % i == 0):
        for j in range(2, (i//2)+2):#checks if the divisor is a prime number (plus 2 so it doesn't skip the number 2)
            if (i % j == 0 and j != i):#if the divisor is divisible by a number that isn't itself then it isn't prime
                prime = False
        if prime == True:
            n = n//i
            while (n % i == 0 and n > 1):#while it's divisible by a number again
                n = n//i
                counter = counter + 1#counter for the powers of a number
            if counter > 1:
                print(str(i)+"^"+str(counter), end = " * ")#convert them to string and add them to make it look better
            else:
                if (n == 1):#to not print * if it's the last number
                    print(i, end = " ")
                else:
                    print(i, end = " * ")
        prime = True#resetting the flag and counters
        counter = 1
    if (n == original and (i + 1) >= (original//2)+1):#if the number itself is prime, then print it
        print(n)
