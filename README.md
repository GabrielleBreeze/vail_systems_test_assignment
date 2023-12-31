# vail_systems_test_assignment
Pre-interview coding submission –
Software Engineer, Test & Infrastructure II

Please provide a code example for review by solving the following problem. The code may be written in a
language of your choice that you are capable of executing. Please submit the solution to either GitHub in
an accessible location and provide a link through email.

The problem we would like you to solve deals with an array of integers. We want to rotate these integers
to a specified number of positions to the left.

If for example you have an array of integers [1,2,3,4,5,6,7] and we would like to rotate 2 positions to the
left, the solution expected would be [3,4,5,6,7,1,2].

Note: the solution should be able to handle a position value greater than the number of integers in the
array. If, for example, we would like to rotate [1,2,3,4,5,6,7] 8 positions to left, it would produce the
result [2,3,4,5,6,7,1]. Negative values for the positions to rotate will throw an error which the code
example should handle gracefully.

Thank you for your effort on this assignment and interest in Vail Systems! Please return this assignment
within 2-3 business days.

Candidate input:

You can find two separate files with different approaches for solvinf this problem. I intentionally added both solutions.
In my opinion version which includes 'while' loop is more efficient and readable for next reasons:
* Operations '.pop' and '.append' both have O(1) complexity
* Worst case scenario for 'while' loop will give O(n-1)
* In matter of readability, using 'while' loop is more generic, launguage agnostic approach.
