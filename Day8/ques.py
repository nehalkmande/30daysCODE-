# Input arrays A and B
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Merge the two arrays
merged_array = A + B

# Calculate the sum of the elements in the merged array
array_sum = sum(merged_array)

# Print the sum
print("Sum of the merged array:", array_sum)


# Input arrays A and B
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Merge the two arrays
merged_array = A + B

# Initializing the product to 1
product = 1

#  product of elements in the merged array
for num in merged_array:
    product *= num

# Print the product
print("Product of the merged array:", product)


from sympy import primerange

# Function to find prime numbers in an array
def find_primes_in_array(arr):
    max_value = max(arr)
    primes = list(primerange(2, max_value + 1))
    return [num for num in arr if num in primes]

# Test Cases
test_cases = [
    [1, 2, 5, 4, 0],   # Test Case 1
    [1, 2, 3, 4, 5],   # Test Case 2
]

for i, test_case in enumerate(test_cases, 1):
    prime_numbers = find_primes_in_array(test_case)
    print(f"Prime numbers in Test Case {i}:", prime_numbers)

