def find_max(arr):
    if not arr:
        return "Array is empty"
    
    max_value = arr[0]  # Assume the first element is the maximum
    
    for num in arr:
        if num > max_value:
            max_value = num
    
    return max_value

# Example usage:
arr = [1, 2, 3, 4, 5]
max_element = find_max(arr)
print("Maximum element:", max_element)  # Output: 5




def find_second_max(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    
    max_value = float('-inf')
    second_max = float('-inf')
    
    for num in arr:
        if num > max_value:
            second_max = max_value
            max_value = num
        elif num > second_max and num != max_value:
            second_max = num
    
    if second_max == float('-inf'):
        return "There is no second maximum element"
    
    return second_max

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 4, 4, 5]
arr3 = [1, 2, 4, 3, 5]

print("Second max in arr1:", find_second_max(arr1))  # Output: 4
print("Second max in arr2:", find_second_max(arr2))  # Output: 4
print("Second max in arr3:", find_second_max(arr3))  # Output: 4
