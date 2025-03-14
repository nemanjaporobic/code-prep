def bucket_sort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


if __name__ == '__main__':
    array = [0, 2, 1, 1, 0, 1, 2, 0, 1, 2, 2]
    array = bucket_sort(array)
    print(f'Result of merge_sort algorithm: {array}')