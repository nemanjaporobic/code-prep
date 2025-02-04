# Function to return the maximum water that can be stored
def maxWater(arr):
    st = []
    res = 0

    for i in range(len(arr)):

        # Pop all items smaller than arr[i]
        while st and arr[st[-1]] < arr[i]:
            pop_height = arr[st.pop()]

            if not st:
                break

            # arr[i] is the next greater for the removed item
            # and new stack top is the previous greater
            distance = i - st[-1] - 1

            # Take the minimum of two heights (next and prev greater)
            water = min(arr[st[-1]], arr[i])

            # Find the amount of water
            water -= pop_height

            res += distance * water
        st.append(i)

    return res


# Driver code
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxWater(arr))