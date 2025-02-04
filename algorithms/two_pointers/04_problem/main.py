class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Two left pointers
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move i
                i += 1
            j += 1  # Always move j

        return i == len(s)  # If i reached the end, s is a subsequence


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().is_subsequence(s, t))

    s = "axc"
    t = "ahbgdc"
    print(Solution().is_subsequence(s, t))
