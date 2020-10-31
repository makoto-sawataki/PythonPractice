# this programm is how to get the numerous of greatest common divisor
#
# input     : a,b
# output    : G 
#

## paturn1 
def func_GCD(a, b):                     # define the function which name is 'func_GCD'

    if a < b:                           # input a and b, when the number b is larger than a, switch them
        a, b = b, a                     # that is a = b, b = a
    x = b 

    while True:
        if a % x == 0 and b % x == 0 :  # if a is equal to 0 and b is also 0, then the greatest common number is x. 
            return x
        x -= 1                          # if not, x is declined by 1 and loop it while the judgement is 'True' 

# input arbitrrary numbers
num1 = input('enter the number: ')
num1 = int(num1)

num2 = input('enter the next number: ')
num2 = int(num2)

print('the greatest number is... ')

# use func_GCD and print the output
print( func_GCD(num1, num2) )


