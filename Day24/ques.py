def find_pairs_with_sum(arr, key):
    pairs = []  # Create an empty list to store pairs
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == key:
                pairs.append((arr[i], arr[j]))  # Add the pair to the result
    
    return pairs

# Example usage:
arr = [2, 3, 4, 5, 6, 7]
key = 10
pairs = find_pairs_with_sum(arr, key)
print("Pairs with a sum of", key, ":", pairs)
