#factorials are right and the sin and cos variables are starting at the right value, but it still isn't giving the right answers at the end
def factorial(b):
    f = 1
    for i in range(1,b+1):
        f = f*i
    return f

x = float(input("Please enter the value: "))
terms = int(input("Please enter the number of terms: "))

sin = x
cos = 1

addition = False

for i in range(2,terms+2, 1):
    divisor = factorial(2*(i-1))#divisors are matching to factorials    
    divisor2 = factorial((2*(i-1))+1)

    if (i % 2) == 0:#on every even run of the program do the subtraction of values
        sin = sin + (x**(i+1)/divisor2)
        cos = cos + ((x**i)/divisor)
    else:#on every odd attempt do the addition of values
        sin = sin - (x**(i+1)/divisor2)
        cos = cos - ((x**i)/divisor)

print("Sin(x) =", sin)
print("Cos(x) =", cos)