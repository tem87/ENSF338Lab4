#ENSF 338 Exercise 7
#2)
def reverse(self):
    current = self.head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    self.head = prev
#3) time both 
import timeit

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Provided implementation
def reverse_original(size):
    new_head = None
    prev_node = None

    for i in range(size - 1, -1, -1):
        curr_node = Node(i)
        curr_new_node = Node(curr_node.data)

        if new_head is None:
            new_head = curr_new_node
        else:
            prev_node.next = curr_new_node

        prev_node = curr_new_node

    return new_head

# Optimized implementation
def reverse_optimized(size):
    current = None
    prev = None

    for i in range(size):
        current = Node(i)
        current.next = prev
        prev = current

    return current

# Function to run the tests
def run_tests(list_size):
    # Test the original implementation
    original_time = timeit.timeit(lambda: reverse_original(list_size), number=100)

    # Test the optimized implementation
    optimized_time = timeit.timeit(lambda: reverse_optimized(list_size), number=100)

    print(f"List Size: {list_size}")
    print(f"Original Time: {original_time:.6f} seconds")
    print(f"Optimized Time: {optimized_time:.6f} seconds")
    print()

# Run tests for different list sizes
for size in [1000, 2000, 3000, 4000]:
    run_tests(size)
#4) plot both
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Provided implementation
def reverse_original(size):
    new_head = None
    prev_node = None

    for i in range(size - 1, -1, -1):
        curr_node = Node(i)
        curr_new_node = Node(curr_node.data)

        if new_head is None:
            new_head = curr_new_node
        else:
            prev_node.next = curr_new_node

        prev_node = curr_new_node

    return new_head

# Optimized implementation
def reverse_optimized(size):
    current = None
    prev = None

    for i in range(size):
        current = Node(i)
        current.next = prev
        prev = current

    return current

# Function to run the tests
def run_tests(list_size):
    # Test the original implementation
    original_time = timeit.timeit(lambda: reverse_original(list_size), number=100)

    # Test the optimized implementation
    optimized_time = timeit.timeit(lambda: reverse_optimized(list_size), number=100)

    return original_time, optimized_time

# List sizes to test
list_sizes = [1000, 2000, 3000, 4000]

# Run tests and collect results
original_times = []
optimized_times = []

for size in list_sizes:
    original_time, optimized_time = run_tests(size)
    original_times.append(original_time)
    optimized_times.append(optimized_time)

# Plot the results
plt.plot(list_sizes, original_times, label='Original')
plt.plot(list_sizes, optimized_times, label='Optimized')
plt.xlabel('List Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.title('Execution Time Comparison')
plt.show()


