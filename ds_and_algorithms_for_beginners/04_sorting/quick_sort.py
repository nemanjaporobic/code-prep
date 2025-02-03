def quick_sort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quick_sort(arr, s, left - 1)

    # Quick sort right side
    quick_sort(arr, left + 1, e)

    return arr


if __name__ == "__main__":
    array = [4, 2, 5, 6, 7, 1, 9, 9, 8, 3, 4]
    array = quick_sort(array, 0, len(array) - 1)
    print(f'Result of merge_sort algorithm: {array}')