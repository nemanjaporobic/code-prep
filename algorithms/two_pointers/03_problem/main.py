from typing import List

class Solution:
    def move_zeros(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(Solution().move_zeros(nums))

    nums = [0]
    print(Solution().move_zeros(nums))
