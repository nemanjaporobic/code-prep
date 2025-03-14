class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap vowels at left and right pointers
            s[left], s[right] = s[right], s[left]

            # Move pointers inward
            left += 1
            right -= 1

        return "".join(s)  # Convert list back to string


if __name__ == '__main__':
    s = "IceCreAm"
    print(Solution().reverse_vowels(s))

    s = "leetcode"
    print(Solution().reverse_vowels(s))
