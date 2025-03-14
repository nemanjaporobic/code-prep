from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        free_spots = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    free_spots += 1

                    if free_spots >= n:
                        return True
        return free_spots >= n


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(Solution().can_place_flowers(flowerbed, n))

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(Solution().can_place_flowers(flowerbed, n))
