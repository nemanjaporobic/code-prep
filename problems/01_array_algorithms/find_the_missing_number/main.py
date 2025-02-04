def find_missing_number(arr, N):
    # Calculate the expected sum of numbers from 1 to N
    total_sum = N * (N + 1) // 2

    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)

    # The missing number is the difference between the expected and actual sum
    missing_number = total_sum - actual_sum

    return missing_number


if __name__ == "__main__":
    arr1 = [1, 2, 4, 6, 3, 7, 8]
    N1 = 8
    print(f"Missing number in arr1: {find_missing_number(arr1, N1)}")

    arr2 = [1, 2, 3, 5]
    N2 = 5
    print(f"Missing number in arr2: {find_missing_number(arr2, N2)}")

# Code Complexity:
# Time Complexity: O(N)
#
# The sum of the array is computed in O(N) time (i.e., iterating through the array once).
# The calculation of the sum of the first N natural numbers is done in constant time O(1).
# Overall, the time complexity is dominated by the array sum computation, so it is O(N).
# Space Complexity: O(1)
#
# Only a few variables (total_sum, actual_sum, missing_number) are used for the computation,
# so the space complexity is constant, O(1).

# Conclusion:
# This is an optimal solution for finding the missing number using the sum formula, with linear time complexity
# and constant space complexity.
