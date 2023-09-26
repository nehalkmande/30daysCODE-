def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False
    return True

# Example usage:
arr1 = [1, 2, 3, 4, 3, 5]
arr2 = [3, 4, 5, 6, 9]

print("Is arr1 sorted?", is_sorted(arr1))
print("Is arr2 sorted?", is_sorted(arr2))
