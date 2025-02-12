class Solution:
    def reverse_words(self, s: str) -> str:
        n = len(s)
        i = 0
        words = []

        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1

            if i >= n:  # If end is reached after skipping spaces
                break

            # Get the word
            start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[start:i])  # Extract and store the word

        # Reverse the list and join with a single space
        return ' '.join(reversed(words))


if __name__ == "__main__":
    s = "the sky is blue"
    print(Solution().reverse_words(s))

    s = "  hello world  "
    print(Solution().reverse_words(s))

    s = "a good   example"
    print(Solution().reverse_words(s))
