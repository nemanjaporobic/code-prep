Trapping Rain Water Problem – Tutorial with Illustrations
Last Updated : 25 Sep, 2024
Trapping Rainwater Problem states that given an array of n non-negative integers arr[] 
representing an elevation map where the width of each bar is 1, compute how much water it can trap after rain.

Examples:
Let us understand Trapping Rainwater problem with the help of some examples:  

Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.


Input: arr[] = {1, 2, 3, 4}
Output: 0
Explanation : We cannot trap water as there is no height bound on both sides


Input: arr[] = {10, 9, 0, 5}
Output: 5
Explanation : We trap 0 + 0 + 5 + 0 = 5


Observations:
The basic intuition of the problem is as follows:
 - An element of the array can store water if there are higher bars on the left and the right. 
 - The amount of water to be stored in every position can be found by finding the heights of the higher bars on the 
    left and right sides. 
 - The total amount of water stored is the summation of the water stored in each index. 
 - No water can be filled if there is no boundary on both sides.

Brute Force – O(n2) Time and O(1) Space:
Traverse every array element and find the highest bars on the left and right sides. 
Take the smaller of two heights. The difference between the smaller height and the height of the current 
element is the amount of water that can be stored in this array element.

Using Stack – O(n) Time and O(n) Space:
We have already discussed a better approach than this, but this is really an interesting approach to learn. It is strongly recommended to refer next greater element, previous greater element and largest area in a histogram problems before moving forward. When we compute next greater element, we pop an item from the stack and mark current item as next greater of it. One important observation here is the item below every item in stack is the previous greater element. So for every element, we can compute both previous greater and next greater in one traversal and a stack. Now you must be wondering that for the trapping rain water problem, we need greatest on right and left (not closest greater). Please pause reading for a moment and thing how we can use next greater and previous greater for finding the amount of water.

As discussed above, the idea is to find next greater and previous greater for every element using a stack and single traversal.
When we have valid next greater and previous greater, we know for sure that we need to fill water between next greater and previous greater. We know a minimum amount also, so we fill the known amount. And when we consider previous greater and next greater we find their next and previous greater, and fill some more amount. We do this until we find next greatest and previous greatest.
We do not fill the exact amount in a go and we also do not necessarily fill one by one, we fill all between next greater and previous greater.

