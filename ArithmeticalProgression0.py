#ArithmeticProgression0.py
# without using any liblaries
# This program shows how to solve an arithmetical progression 
# such as  "a_n = d*n + a_1".
# The demostration program solves "a_n = 3*n - 5"
a0 = -5
an = 0
n = int(input())
i = 0

while i <= n:
    an = an + a0
    print(an)

    i += 1

