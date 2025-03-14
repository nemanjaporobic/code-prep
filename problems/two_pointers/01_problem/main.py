class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        result = []
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                result.append(word1[w1])
                w1 += 1
            if w2 < len(word2):
                result.append(word2[w2])
                w2 += 1
        return ''.join(result)


if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    print(Solution().merge_alternately(word1, word2))

    word1 = "ab"
    word2 = "pqrs"
    print(Solution().merge_alternately(word1, word2))

    word1 = "abcd"
    word2 = "pq"
    print(Solution().merge_alternately(word1, word2))


