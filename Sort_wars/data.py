# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html

import numpy
import os

# Create a directory if it does not exits
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# generating the arrays using numpy
def generate_random_numbers(size):
    return numpy.random.randint(100000, 1000000, size=size)

def generate_reversed_random_numbers(size):
    numbers = numpy.arange(999999, 999999-size, -1)
    return numbers

# generating the numbers
random_10k = generate_random_numbers(10000)
random_100k = generate_random_numbers(100000)
reversed_10k = generate_reversed_random_numbers(10000)
reversed_100k = generate_reversed_random_numbers(100000)

#saving the datasets
numpy.save('datasets/random_10k.npy', random_10k)
numpy.save('datasets/random_100k.npy', random_100k)
numpy.save('datasets/reversed_10k.npy', reversed_10k)
numpy.save('datasets/reversed_100k.npy', reversed_100k)