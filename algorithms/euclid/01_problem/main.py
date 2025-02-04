class Solution:
    def gcd_of_string(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcd_of_string(str1, str2))

    str1 = "ABABAB"
    str2 = "ABAB"
    print(Solution().gcd_of_string(str1, str2))

    str1 = "LEET"
    str2 = "CODE"
    print(Solution().gcd_of_string(str1, str2))
