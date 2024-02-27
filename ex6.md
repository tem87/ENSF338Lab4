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

Sources:
Pandey, K. (2022, December 7). Array vs Linked List [When to use What]. Retrieved February 16, 2024, from Masai School website: https://www.masaischool.com/blog/array-vs-linked-list-when-to-use-what/#:~:text=Here%20we%20can%20see%20that,pointers%20to%20the%20other%20nodes 

Krohn, H. (2019, July 2). Linked Lists vs. Arrays - Towards Data Science. Retrieved February 16, 2024, from Medium website: https://towardsdatascience.com/linked-lists-vs-arrays-78746f983267

‌
### 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? 
The use of pointers to keep track o the position of each element of the array can minimize the times.

### 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them: insertion and merge sort.

### 4. Also show the expected complexity for each and how it differs from applying it to a regular array

It is possible to use both insertion and merge sort for both cases. For insertion sort, we have direct access to the previous and next node, making it easier to insert each node at a specific position. The complexity is O(n^2), but it is efficient and stable.

For merge sort, we can find the middle node, divide the doubly linked list into two halves, sort them, and merge them. The complexity is O(n log(n)). Handling the pointers when doing the sub lists can be more complex. 

Insertion sort could be more efficient when dealing with a smaller doubly linked list compared to merge sort and when dealing with a larger size of nodes, merge sort could be a better alternative. It depends on the application and requirements.

The difference between implementing merge sort with arrays, is that you need a temporary array, O(n) extra memory and wiht the doubled linked list. 






