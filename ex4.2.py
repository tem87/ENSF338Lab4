#ENSF 338 Lab 4 Exercise 4.2 (COMPLETE)

'''
QUESTION 4
The worst case complexity of the inefficient search algorithm, which is
a linear search is O(n).

The worst case complexity of the efficient search algorithm is O(log(n)).
'''

#Inefficient Code
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#Efficient Code
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

import time
import random
import matplotlib.pyplot as plt

# Function to generate a sorted array
def generate_sorted_array(size):
    return sorted(random.sample(range(size * 3), size))

# Time measurement function
def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time

# Perform measurements
sizes = [1000, 2000, 3000, 4000, 5000]
num_measurements = 100

linear_search_times = []
binary_search_times = []

for size in sizes:
    arr = generate_sorted_array(size)
    target = random.randint(0, size * 3)

    linear_times = []
    binary_times = []

    for _ in range(num_measurements):
        linear_time = measure_time(linear_search, arr, target)
        binary_time = measure_time(binary_search, arr, target)

        linear_times.append(linear_time)
        binary_times.append(binary_time)

    linear_search_times.append(sum(linear_times) / num_measurements)
    binary_search_times.append(sum(binary_times) / num_measurements)

# Plotting
plt.plot(sizes, linear_search_times, label="Linear Search")
plt.plot(sizes, binary_search_times, label="Binary Search")
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Comparison of Linear Search and Binary Search')
plt.legend()
plt.show()
