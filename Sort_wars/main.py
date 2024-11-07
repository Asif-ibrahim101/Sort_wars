import time
import random
import memory_profiler
import matplotlib.pyplot as plot

#function for generating random datasets
def generate_random_dataset(size):
    dataset = []
    for i in range(1, size):
        number = random.randint(100000, 999999)
        dataset.append(number)
    return dataset;

# function for generating reversed_datasset
def generate_reversed_dataset(size):
    start_number = 999999
    end_number = start_number - size -1
    dataset = list(range(start_number, end_number, -1))
    return dataset

# generating the numbers
random_dataset_10000 = generate_random_dataset(10000)
random_dataset_100000 = generate_random_dataset(100000)

# generating reversed numbers
reversed_dataset_10000 = generate_reversed_dataset(10000)
reversed_dataset_100000 = generate_reversed_dataset(100000)


# verifying the datasets
print("randdom datasets (10,000 elements): ", random_dataset_10000[:10])
print("randdom datasets (100,000 elements): ", random_dataset_100000[:10])

print("Reversed Datassets (10,000): ", reversed_dataset_10000[:10])
print("Reversed Datassets (100,000): ", reversed_dataset_100000[:10])