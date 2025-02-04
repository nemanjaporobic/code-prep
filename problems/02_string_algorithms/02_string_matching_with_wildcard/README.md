Wildcard Pattern Matching
Last Updated : 17 Sep, 2024
Given a text t and a wildcard pattern p, implement wildcard pattern matching algorithm that finds if wildcard pattern is matched with text. The matching should cover the entire text (not partial text). The wildcard pattern can include the characters ‘?’ and ‘*’ 

‘?’ – matches any single character 
‘*’ – Matches any sequence of characters (including the empty sequence)

Examples:

    Input :  t = “abcde”, p = “a?c*” 
    Output : Yes
    Explanation : ? matches with b and * matches with “de”

    Input :  t = “abcde”, p = “e?c*” 
    Output : No

    Input :  t = “abc”, p = “*” 
    Output : Yes