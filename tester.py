import random
random.seed(3)
my_array = [random.randint(0, 99) for i in range(20)]

my_array
from SelectionSort import selection_sort

selection_sort(my_array)
my_array