# find greatest common divisor from integer a and b
#
# Use Euclidean algorithm
# 1. let integer a and b
# 2. b divides a and find its remainder r
# 3. if r is equal to 0, then b is the greatest common divisor
# 4. b assigns into a, r assigns into b, then back to 3.

def func_euclidean(a, b) :
    r = a % b
    if r == 0:
        return b
    return func_euclidean(b, r)

# input arbitrrary numbers
num1 = input('enter the number: ')
num1 = int(num1)

num2 = input('enter the next number: ')
num2 = int(num2)

print('the greatest number is... ')

# use func_euclidean and print the output
print( func_euclidean(num1, num2) )
