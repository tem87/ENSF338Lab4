# ANSWET TO Q4
'''
The complexity of binary seacrh for linked list is O(n), you need to 
traverse the list to find the element that you are looking for.
'''


import matplotlib.pyplot as plt
import timeit

# Class code
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Class linked list
class LinkedList:
    def __init__(self):
        self.head = None
    #used chatgpt    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def binary_search(self, num):
        current = self.head
        index = 0
        while current:
            if current.data == num:
                return index
            current = current.next
            index += 1
        return -1
    #end of chatgpt

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Class array list
class Array:
    def __init__(self):
        self.array = []

    def append(self, data):
        self.array.append(data)

    def binary_search(self, num):
        low, high = 0, len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == num:
                return mid
            elif self.array[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def print_array(self):
        print("Array:", self.array)

sizes = [1000, 2000, 4000, 8000]

def performance(data_structure, input_sizes):
    times = []
    for size in input_sizes:
        data_structure_instance = data_structure()
        for i in range(size):
            data_structure_instance.append(i)

        # Print 
        #if isinstance(data_structure_instance, LinkedList):
        #    data_structure_instance.print_list()
        #elif isinstance(data_structure_instance, Array):
        #    data_structure_instance.print_array()

        time_taken = timeit.timeit(lambda: data_structure_instance.binary_search(size // 2), number=1000)
        times.append(time_taken)

    return times

linked_list_times = performance(LinkedList, sizes)
array_times = performance(Array, sizes)

plt.plot(sizes, linked_list_times, label='Linked List')
plt.plot(sizes, array_times, label='Array')
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.legend()
plt.show()
