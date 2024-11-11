Edit Distance
Last Updated : 21 Aug, 2024
Given two strings s1 and s2 of lengths m and n respectively and below operations that can be performed on s1. 
Find the minimum number of edits (operations) to convert ‘s1‘ into ‘s2‘.  

Insert: Insert any character before or after any index of s1
Remove: Remove a character of s1
Replace: Replace a character at any index of s1 with some other character.
Note: All of the above operations are of equal cost. 

Examples: 

    Input:   s1 = “geek”, s2 = “gesek”
    Output:  1
    Explanation: We can convert s1 into s2 by inserting a ‘s’ between two consecutive ‘e’ in s2.

    Input:   s1 = “cat”, s2 = “cut”
    Output:  1
    Explanation: We can convert s1 into s2 by replacing ‘a’ with ‘u’.


    Input:   s1 = “sunday”, s2 = “saturday”
    Output:  3
    Explanation: Last three and first characters are same.  We basically need to convert “un” to “atur”. 
    This can be done using below three operations. Replace ‘n’ with ‘r’, insert t, insert a