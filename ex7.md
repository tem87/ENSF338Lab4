#### 1. Give an expression for the time complexity of the reverse() implementation. Explain how you reached the conclusion describing your step-by-step reasoning. [0.3 pts]

The time complexity of the reverse implementation is O(n). In the function there is a for loop which contains an if else statement. The for loop will be run for the length of the list and either the if statement or the else statement will be run once during each iteration. This leaves us with a complexity of O(n).

#### 2. Design an optimized implementation of the same function with better performance. Discuss which changes you made and how they should be expected to result in a better function [0.3 pts]
The optimized version of the code does not create new nodes rather it updates the next pointers of the existing nodes to reverse the direction of the list. It traverses the list once to update the pointers but eliminates the need to do a second round for creating new nodes. It reduces the constant factors associated with memory allocation and improves the efficiency of the reversal process. 
