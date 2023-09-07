# Test cases
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

sum_A = sum(A)
sum_B = sum(B)

print("Sum of A:", sum_A)
print("Sum of B:", sum_B)


# Test cases
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Merge the arrays
merged_array = A + B

print("Merged Array:", merged_array)


# Function to separate even and odd numbers in an array using list comprehensions
def separate_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    return even_numbers, odd_numbers

# Test cases
A = [1, 2, 5, 4, 0]
B = [1, 2, 5, 4, 0]

even_A, odd_A = separate_even_odd(A)
even_B, odd_B = separate_even_odd(B)

print("Even numbers in A:", even_A)
print("Odd numbers in A:", odd_A)
print("Even numbers in B:", even_B)
print("Odd numbers in B:", odd_B)
