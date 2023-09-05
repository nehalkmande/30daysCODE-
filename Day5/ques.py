# Arrays to be sorted
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Sorting arrays A and B
sorted_A = sorted(A)
sorted_B = sorted(B)

print("Sorted A:", sorted_A)
print("Sorted B:", sorted_B)


# Key to search
key = 1

# Arrays
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# first occurrence of key in array A
index_A = A.index(key) if key in A else -1

# first occurrence of key in array B
index_B = B.index(key) if key in B else -1

print("Index of key in array A:", index_A)
print("Index of key in array B:", index_B)


# Testcases
A1 = [1, 2, 5, 4, 0]
B1 = [1, 2, 5, 4, 0]

A2 = [1, 2, 3, 4, 5]
B2 = [11, 22, 33, 44]

# Function to separate even and odd numbers in an array
def separate_even_odd(arr):
    even = [num for num in arr if num % 2 == 0]
    odd = [num for num in arr if num % 2]
    return even, odd

# Separating even and odd numbers for Testcase 1
even_A1, odd_A1 = separate_even_odd(A1)
even_B1, odd_B1 = separate_even_odd(B1)

# Separating even and odd numbers for Testcase 2
even_A2, odd_A2 = separate_even_odd(A2)
even_B2, odd_B2 = separate_even_odd(B2)

# Printing results
print("Testcase 1:")
print("Even numbers in A1:", even_A1)
print("Odd numbers in A1:", odd_A1)
print("Even numbers in B1:", even_B1)
print("Odd numbers in B1:", odd_B1)

print("\nTestcase 2:")
print("Even numbers in A2:", even_A2)
print("Odd numbers in A2:", odd_A2)
print("Even numbers in B2:", even_B2)
print("Odd numbers in B2:", odd_B2)
