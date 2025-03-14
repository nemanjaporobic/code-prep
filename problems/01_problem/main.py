from typing import List


class Solution:
    def kids_with_candies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candy + extraCandies >= max(*candies) for candy in candies]


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(Solution().kids_with_candies(candies, extraCandies))

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(Solution().kids_with_candies(candies, extraCandies))

    candies = [12, 1, 12]
    extraCandies = 10
    print(Solution().kids_with_candies(candies, extraCandies))

