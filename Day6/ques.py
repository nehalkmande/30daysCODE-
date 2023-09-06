A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Find the common elements using set intersection
common_elements = list(set(A) & set(B))

# Print the common elements
print("Common elements:", common_elements)


A = [0, 1, 2, 6, 4, 5]
B = [5, 4, 3, 2, 9, 0]

# Convert both arrays to sets
set_A = set(A)
set_B = set(B)

# Find the missing numbers by taking the difference of sets
missing_in_A = list(set_B - set_A)
missing_in_B = list(set_A - set_B)

# Print the missing numbers in both arrays
print("Missing in A:", missing_in_A)
print("Missing in B:", missing_in_B)


def find_single_element(arr):
    result = 0
    
    for num in arr:
        result ^= num
        
    return result

# Test cases
testcase1 = [1, 1, 3, 3, 3, 0]
testcase2 = [1, 2, 2, 2, 2, 2, 2]

result1 = find_single_element(testcase1)
result2 = find_single_element(testcase2)

print("Result 1:", result1)
print("Result 2:", result2)
