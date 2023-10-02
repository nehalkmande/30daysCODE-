def rotate_array(arr, k):
    n = len(arr)
    
    # k is within the range [0, n)
    k = k % n
    
    # rotation using slicing
    rotated_arr = arr[-k:] + arr[:-k]
    
    return rotated_arr

# Example usage:
original_arr = [1, 2, 3, 4, 5]
k = 2  # Rotate by 2 times to the right

rotated_arr = rotate_array(original_arr, k)
print(rotated_arr)  
