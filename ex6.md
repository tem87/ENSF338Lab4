1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) 
Accesing an element
For arrays we have O(1) complexity because we only need the index. However for linked lists we need to traverse from the first node, with a time complexity of O(n).

Inserting an element
Time complexity for arrays will be proportional to the size of the array, O(n). We could get O(1) if we are inserting the element at the end. For linked lists, we have a time complexity of O(1)

The advantages of implementing arrays:
Simple to use and retrievals and replacements are quick if the index is known.
Disadvantages: 
y having a fixed sized we might waste space or be limited. 
inserting and deleting can be very slow.

Advantages of Linked list
Better used of memory, size is not pre-defined.
Fast insertion and deletion time, O(1)
Disadvantage
Slower search time, you need to iterate when you are searching for an element.

Pandey, K. (2022, December 7). Array vs Linked List [When to use What]. Retrieved February 16, 2024, from Masai School website: https://www.masaischool.com/blog/array-vs-linked-list-when-to-use-what/#:~:text=Here%20we%20can%20see%20that,pointers%20to%20the%20other%20nodes.

Krohn, H. (2019, July 2). Linked Lists vs. Arrays - Towards Data Science. Retrieved February 16, 2024, from Medium website: https://towardsdatascience.com/linked-lists-vs-arrays-78746f983267

‌

2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. 
How can this function be implemented to minimize the impact of each of the standalone tasks? 

3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it possible or not to use them. 
1. Insertion sort
2. Merge sort

4. Also show the expected complexity for each and how it differs from
applying it to a regular array