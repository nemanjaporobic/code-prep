Minimum Platforms Required for Given Arrival and Departure Times
Last Updated : 02 Sep, 2024
We are given two arrays that represent the arrival and departure times of trains, 
the task is to find the minimum number of platforms required so that no train waits.

Examples:

    Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}, dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
    Output: 3 
    Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

    Input: arr[] = {9:00, 9:40}, dep[] = {9:10, 12:00} 
    Output: 1 
    Explanation: Only one platform is needed. 