### 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) 
*Accesing an element*
For arrays we have O(1) complexity because we only need the index. However, for linked lists we need to traverse from the first node, with a time complexity of O(n).

*Inserting an element*
Time complexity for arrays will be proportional to the size of the array, O(n). We could get O(1) if we are inserting the element at the end. For linked lists, we have a time complexity of O(1).

**ARRAYS**

*Advantages*
-Simple to use and retrievals and replacements are quick if the index is known O(1).

*Disadvantages* 
-Having a fixed sized we might waste space or be limited. 
-Inserting and deleting can be very slow.
-Dynamic sized arrays requires copying, next memory might not be free, we could have a flexibility penalty. 

**LINKED LISTS**

*Advantages*
-Better used of memory, size is not pre-defined.
-Fast insertion and deletion time, O(1).

*Disadvantages*
-Slower search time, you need to iterate when you are searching for an element.
Not indexable anymore.

**Sources**

Pandey, K. (2022, December 7). Array vs Linked List [When to use What]. Retrieved February 16, 2024, from Masai School website: https://www.masaischool.com/blog/array-vs-linked-list-when-to-use-what/#:~:text=Here%20we%20can%20see%20that,pointers%20to%20the%20other%20nodes 

Krohn, H. (2019, July 2). Linked Lists vs. Arrays - Towards Data Science. Retrieved February 16, 2024, from Medium website: https://towardsdatascience.com/linked-lists-vs-arrays-78746f983267

‌
### 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? 

To minimize the impact of each standalone task, we could keep track of the position of each element in the array, using pointers. This approach allows for direct access to memory locations. Although the complexity remains O(n) due to the need for implementing a loop.

Alternatively, we could opt for a different data structure, such as linked lists. As discussed in question 1, linked lists offer O(1) complexity for insertion and deletion operations.

Another implementation involves utilizing the 'pop' function, which efficiently removes an element at a specified index:
def delete(arr, index):
    arr.pop(index)

Following the deletion, insertion can be seamlessly implemented.


### 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them: insertion and merge sort.

It is possible to use both insertion and merge sort for both cases. For insertion sort, we have direct access to the previous and next node, making it easier to insert each node at a specific position. The complexity is O(n^2) in the worst case and average case and O (n) in the best case. It is efficient and stable.

For merge sort, we can find the middle node, divide the doubly linked list into two halves, sort them, and merge them. The complexity is O(n log(n)). Handling the pointers when doing the sub lists can be more complex. 

Insertion sort could be more efficient when dealing with a smaller doubly linked list compared to merge sort and when dealing with a larger size of nodes, merge sort could be a better alternative. It depends on the application and requirements.


### 4. Also show the expected complexity for each and how it differs from applying it to a regular array
The complexity is addressed in question three. 

The distinction between these two data structures lies in the efficiency of insertion, which is greater in doubly linked lists due to the use of pointers. However, the access time for finding the correct position in the list is slower than that in arrays.

As for merge sort, the complexity remains the same for both data structures. However, inserting a node in the correct position takes only O(1) time, making it faster. Merge sort has a space complexity of O(n) for doubly linked lists and arrays.

In real-life implementation, the performance of both algorithms might differ.


**Sources for Question 3 and 4**

1. Sharma, A. (2021, August 6). Learn to implement Insertion Sort technique for Doubly Linked List. Retrieved February 29, 2024, from PrepBytes Blog website: https://www.prepbytes.com/blog/linked-list/insertion-sort-for-doubly-linked-list/ 

2. GfG. (2017, July 5). Insertion Sort for Doubly Linked List. Retrieved February 29, 2024, from GeeksforGeeks website: https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/

3. GfG. (2015, May 2). Merge Sort for Doubly Linked List. Retrieved February 29, 2024, from GeeksforGeeks website: https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/

4. Jain, A. (2021, August 19). Learn easy method to Sort Doubly Linked List using Merge Sort. Retrieved February 29, 2024, from PrepBytes Blog website: https://www.prepbytes.com/blog/linked-list/merge-sort-for-doubly-linked-list/#:~:text=Merge%20sort%20is%20a%20popular,produce%20the%20final%20sorted%20array.

5. Coding Ninjas Studio. (2024). Retrieved February 29, 2024, from Codingninjas.com website: https://www.codingninjas.com/studio/library/why-is-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists

‌

‌



‌
‌




