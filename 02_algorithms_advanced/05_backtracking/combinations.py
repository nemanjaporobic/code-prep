# Trivial approach
# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).
# Time: O(k * 2^n)
def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs


def helper(i, cur_comb, combs, n, k):
    if len(cur_comb) == k:
        combs.append(cur_comb.copy())
        return
    if i > n:
        return

    # decision to include i
    cur_comb.append(i)
    helper(i + 1, cur_comb, combs, n, k)
    cur_comb.pop()

    # decision to NOT include i
    helper(i + 1, cur_comb, combs, n, k)


# The most optimal solution
# Time: O(k * C(n, k))
def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs


def helper2(i, cur_comb, combs, n, k):
    if len(cur_comb) == k:
        combs.append(cur_comb.copy())
        return
    if i > n:
        return

    for j in range(i, n + 1):
        cur_comb.append(j)
        helper2(j + 1, cur_comb, combs, n, k)
        cur_comb.pop()
