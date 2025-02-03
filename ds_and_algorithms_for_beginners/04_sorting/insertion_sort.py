from typing import List


def insertion_sort(arr: List) -> List:
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr


if __name__ == "__main__":
    array = [4, 2, 5, 6, 7, 1, 9, 9, 8, 3, 4]
    array = insertion_sort(array)
    print(f'Result of insertion_sort algorithm: {array}')
