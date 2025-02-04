def max_product_subarray(arr):
    # Initialize variables to store the result, current max and min products
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    # Traverse the array from the second element
    for i in range(1, len(arr)):
        # If current element is negative, swap max and min
        if arr[i] < 0:
            max_product, min_product = min_product, max_product

        # Update max_product and min_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])

        # Update the result with the maximum product found so far
        result = max(result, max_product)

    return result


if __name__ == "__main__":
    arr1 = [-2, 6, -3, -10, 0, 2]
    arr2 = [-1, -3, -10, 0, 60]
    print(max_product_subarray(arr1))
    print(max_product_subarray(arr2))
