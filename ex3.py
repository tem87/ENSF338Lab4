#ENSF 338 Exercise 3 - (COMPLETE)

'''
QUESTION 1
The strategy for growing arrays when full is to allocate slightly more 
memory than needed. This is called the grow factor. This is seen in the 
line: 

new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

In this line we make the overallocation proportional to the list size.
It then adds the necessary padding to make it a multiple of 4.  

The grow factor for python is 1.125. 

QUESTION 5
From the graphs we can see that there is a difference in the execution times. 
It takes longer to grow than it does to shrink. That's because when you allocate 
more space, you need to move the entire array in order to fit the space in memory. 
When you shrink an array, you don't have to concern yourself with this. So
S-1 is faster than S+1.
'''

import sys

def check_growth_factor():
    prev_capacity = 0
    for i in range(64):
        lst = list(range(i))
        capacity = sys.getsizeof(lst)
        if capacity != prev_capacity:
            print(f"Capacity changed at {i} elements: {prev_capacity} -> {capacity}")
            prev_capacity = capacity


check_growth_factor()

import timeit
import matplotlib.pyplot as plt

def grow_to_64():
    lst = list(range(63))
    start_time = timeit.default_timer()
    lst.append(63)
    end_time = timeit.default_timer()
    return end_time - start_time

def shrink_to_62():
    lst = list(range(63))
    start_time = timeit.default_timer()
    lst.pop()
    end_time = timeit.default_timer()
    return end_time - start_time

# Measure time to grow to 64
grow_times = [grow_to_64() for _ in range(1000)]

# Measure time to shrink to 62
shrink_times = [shrink_to_62() for _ in range(1000)]

# Plotting
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(grow_times, bins=30, color='blue', alpha=0.7)
plt.title('Time to Grow to 64')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(shrink_times, bins=30, color='green', alpha=0.7)
plt.title('Time to Shrink to 62')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

