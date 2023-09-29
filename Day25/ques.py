def check_sorted(arr):
    #  if the array is sorted in ascending order
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 1
    
    #  if the array is sorted in descending order
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return -1
    
    # If neither condition is met, return 0
    return 0

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 1]

result1 = check_sorted(arr1)  # Returns 1
result2 = check_sorted(arr2)  # Returns -1

print(result1)
print(result2)
