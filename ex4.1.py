#ENSF 338 Lab 4 Exercise 4.1 (COMPLETE)

'''
Question 1:
The best case scenario is when none of the elements in the list
are greater than 5. If this is the case, then the inner loop
is never executed and the function goes through once. Therefore 
the best case complexity is O(n).

The worst case scenario is when all the elements in the list are
less than 5. In this case the loops are fully executed. So the 
resulting complexity is O(n^2)

In the average case, we expect some elements to be greater than 5
and some elements to be less than 5. So we can expect the inner loop
and the outer loop to be executed. Therefore the average case
complexity is O(n^2)
'''


'''
Question 2:
No, the average, best and worst case complexities are not the same. 
Below is a modified version of the code in which all the complexities
will be linear. The inner loop now iterates a fixed number of times (5 in this case), 
regardless of the length of the input list.
'''

import matplotlib.pyplot as plt

def processdata(li):
    for i in range(len(li)):        # O(n)
        if li[i] > 5:               # O(1)
            for j in range(5):      # Fixed number of iterations
                li[i] *= 2          # O(1)

