# Time: O(n^2 * n!)
def permutations_recursive(nums):
    return helper(0, nums)


def helper(i, nums):
    if i == len(nums):
        return [[]]

    res_perms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(j, nums[i])
            res_perms.append(p_copy)
    return res_perms


# Iterative solution
# Time: O(n^2 * n!)
def permutations_iterative(nums):
    perms = [[]]

    for n in nums:
        next_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                next_perms.append(p_copy)
        perms = next_perms
    return perms
