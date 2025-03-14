# Brute Force: O(n^2)
def brute_force(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)
    return max_sum


# Kadane's Algorithm: O(n)
def kadanes(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum


# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def sliding_window(nums):
    max_sum = nums[0]
    cur_sum = 0
    max_l, max_r = 0, 0
    l = 0

    for r in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            l = r

        cur_sum += nums[r]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_l, max_r = l, r

    return [max_l, max_r]
