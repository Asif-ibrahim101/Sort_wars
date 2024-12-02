import sys
sys.setrecursionlimit(10)
import numpy as np
import time
import psutil
import matplotlib.pyplot as plt
import os

if not os.path.exists('results'):
   os.makedirs('results')
   
   
# Selection sort


def merge(left, right):
   result = []
   i = j = 0
   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           result.append(left[i])
           i += 1
       else:
           result.append(right[j])
           j += 1
   result.extend(left[i:])
   result.extend(right[j:])
   return result

def merge_sort(array):
   if len(array) <= 1:
       return array
   mid = len(array) // 2
   left = merge_sort(array[:mid])
   right = merge_sort(array[mid:])
   return merge(left, right)

def partition(array, low, high):
   pivot = array[high]
   i = low - 1
   for j in range(low, high):
       if array[j] <= pivot:
           i += 1
           array[i], array[j] = array[j], array[i]
   array[i + 1], array[high] = array[high], array[i + 1]
   return i + 1

def quick_sort(array):
   def _quick_sort(arr, low, high):
       if low < high:
           pi = partition(arr, low, high)
           _quick_sort(arr, low, pi - 1)
           _quick_sort(arr, pi + 1, high)
   
   arr_copy = array.copy()
   _quick_sort(arr_copy, 0, len(arr_copy) - 1)
   return arr_copy

def test_sorting_algorithm(algorithm, dataset, name):
   try:
       process = psutil.Process()
       memory_before = process.memory_info().rss / 1024 / 1024
       
       start_time = time.time()
       sorted_array = algorithm(dataset.copy())
       end_time = time.time()
       execution_time = (end_time - start_time) * 1000
       
       memory_after = process.memory_info().rss / 1024 / 1024
       memory_used = memory_after - memory_before
       
       return {
           'time': execution_time,
           'memory': memory_used
       }
   except Exception as e:
       print(f"Error in {name}: {str(e)}")
       return {
           'time': 0,
           'memory': 0
       }

try:
   random_10k = np.load('datasets/random_10k.npy')
   random_100k = np.load('datasets/random_100k.npy')
   reversed_10k = np.load('datasets/reversed_10k.npy')
   reversed_100k = np.load('datasets/reversed_100k.npy')
except FileNotFoundError:
   print("Dataset files not found. Run data.py first.")
   exit()

datasets = {
   'Random 10k': random_10k,
   'Random 100k': random_100k,
   'Reversed 10k': reversed_10k,
   'Reversed 100k': reversed_100k
}

results = {}
for name, dataset in datasets.items():
   results[f'Merge Sort - {name}'] = test_sorting_algorithm(merge_sort, dataset, name)
   results[f'Quick Sort - {name}'] = test_sorting_algorithm(quick_sort, dataset, name)

try:
   with open('results/sorting_results.txt', 'w') as f:
       for name, metrics in results.items():
           if metrics:
               f.write(f"\n{name}:\n")
               f.write(f"Time: {metrics['time']:.2f} ms\n")
               f.write(f"Memory: {metrics['memory']:.2f} MB\n")
           else:
               f.write(f"\n{name}: Error during testing\n")
except Exception as e:
   print(f"Error writing results: {str(e)}")

# Time comparison plot
plt.figure(figsize=(10, 6))
names = list(datasets.keys())
merge_times = [results[f'Merge Sort - {name}']['time'] for name in names]
quick_times = [results[f'Quick Sort - {name}']['time'] for name in names]

plt.bar(names, merge_times, width=0.35, label='Merge Sort')
plt.bar([x + 0.35 for x in range(len(names))], quick_times, width=0.35, label='Quick Sort')
plt.xlabel('Dataset')
plt.ylabel('Time (ms)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/time_comparison.png')

# Memory comparison plot
plt.figure(figsize=(10, 6))
merge_memory = [results[f'Merge Sort - {name}']['memory'] for name in names]
quick_memory = [results[f'Quick Sort - {name}']['memory'] for name in names]

plt.plot(names, merge_memory, marker='o', label='Merge Sort')
plt.plot(names, quick_memory, marker='o', label='Quick Sort')
plt.xlabel('Dataset')
plt.ylabel('Memory Usage (MB)')
plt.title('Memory Usage Comparison')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/memory_comparison.png')

print("\nAnalysis complete. Check results folder for detailed output.")
