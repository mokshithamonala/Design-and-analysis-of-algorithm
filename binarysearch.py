def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # integer division

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # Element not found
    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
