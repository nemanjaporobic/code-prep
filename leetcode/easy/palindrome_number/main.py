class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) aren't palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        # Reverse the last half of the digits and compare with the first half
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check for palindrome condition
        return x == reversed_half or x == reversed_half // 10