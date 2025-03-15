def subsets_without_duplicates(nums):
    subsets, cur_set = [], []
    helper(0, nums, cur_set, subsets)
    return subsets


def helper(i, nums, cur_set, subsets):
    if i >= len(nums):
        subsets.append(cur_set.copy())
        return

    # decision to include nums[i]
    cur_set.append(nums[i])
    helper(i + 1, nums, cur_set, subsets)
    cur_set.pop()

    # decision NOT to include nums[i]
    helper(i + 1, nums, cur_set, subsets)


def subsets_with_duplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper2(0, nums, curSet, subsets)
    return subsets


def helper2(i, nums, cur_set, subsets):
    if i >= len(nums):
        subsets.append(cur_set.copy())
        return

    # decision to include nums[i]
    cur_set.append(nums[i])
    helper2(i + 1, nums, cur_set, subsets)
    cur_set.pop()

    # decision NOT to include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, cur_set, subsets)
