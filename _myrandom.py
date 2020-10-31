#random.py
# "This program generates random number and stores them in a array.
import random
random.seed(3)

my_array = [random.randint(0, 99) for i in range(20)]
