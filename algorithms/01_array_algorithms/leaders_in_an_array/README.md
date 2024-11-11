Leaders in an array
Last Updated : 04 Oct, 2024
Given an array arr[] of size n, the task is to print all the Leaders in the array. An element is a Leader if 
it is greater than all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

    Input: arr[] = {16, 17, 4, 3, 5, 2} 
    Output: 17 5 2
    Explanation: 17 is greater than all the elements to its right: 4, 3, 5 and 2, therefore 17 is a leader.
    is greater than all the elements to its right: 2, therefore 5 is a leader. 
    2 has no element to its right, therefore 2 is a leader.

    Input: arr[] = {1, 2, 3, 4, 5, 2} 
    Output: 5 2
    Explanation: 5 is greater than all the elements to its right: 2, therefore 5 is a leader. 
    2 has no element to its right, therefore 2 is a leader.