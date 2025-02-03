# Python implementation of Binary Search
def binary_search(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    while l < r:
        m = (l + r) // 2

        if target > arr[m]:
            l = m + 1
        elif target < arr[m]:
            r = m - 1
        else:
            return m
    return -1


if __name__ == '__main__':
    array = [1, 3, 3, 4, 5, 6, 7, 8]
    result1 = binary_search(array, 4)
    result2 = binary_search(array, 12)
    result3 = binary_search(array, 3)

    print(f'Result of target 4 is: {result1}')
    print(f'Result of target 12 is: {result2}')
    print(f'Result of target 3 is: {result3}')

