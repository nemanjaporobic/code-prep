from typing import List


def merge_sort(arr: List[int], s: int, e: int) -> List:
    if e - s + 1 <= 1:
        return arr

    m = (s + e) // 2

    merge_sort(arr, s, m)
    merge_sort(arr, m + 1, e)

    merge(arr, s, m, e)

    return arr


def merge(arr: List[int], s: int, m: int, e: int) -> None:
    left = arr[s: m + 1]
    right = arr[m + 1: e + 1]

    l = 0
    r = 0
    a = s

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[a] = left[l]
            l += 1
        else:
            arr[a] = right[r]
            r += 1
        a += 1

    while l < len(left):
        arr[a] = left[l]
        l += 1
        a += 1

    while r < len(right):
        arr[a] = right[r]
        r += 1
        a += 1


if __name__ == "__main__":
    array = [4, 2, 5, 6, 7, 1, 9, 9, 8, 3, 4]
    array = merge_sort(array, 0, len(array) - 1)
    print(f'Result of merge_sort algorithm: {array}')
