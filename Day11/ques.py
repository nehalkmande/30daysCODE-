# Given arrays
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

def find_duplicate(arr):
    seen = set()  # Create an empty set to store seen numbers
    for num in arr:
        if num in seen:
            return num  # Found a duplicate
        seen.add(num)  # Add the number to the set
    return None  # No duplicates found

# Find a duplicate in array A
duplicate_A = find_duplicate(A)

# Find a duplicate in array B
duplicate_B = find_duplicate(B)

if duplicate_A is not None:
    print("Duplicate in array A:", duplicate_A)
else:
    print("No duplicates found in array A")

if duplicate_B is not None:
    print("Duplicate in array B:", duplicate_B)
else:
    print("No duplicates found in array B")


# Given arrays
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

def find_duplicate(arr):
    seen = set()  # Create an empty set to store seen numbers
    for num in arr:
        if num in seen:
            return num  # Found a duplicate
        seen.add(num)  # Add the number to the set
    return None  # No duplicates found

# Find a duplicate in array A
duplicate_A = find_duplicate(A)

# Find a duplicate in array B
duplicate_B = find_duplicate(B)

if duplicate_A is not None:
    print("Duplicate in array A:", duplicate_A)
else:
    print("No duplicates found in array A")

if duplicate_B is not None:
    print("Duplicate in array B:", duplicate_B)
else:
    print("No duplicates found in array B")


from collections import defaultdict

def find_duplicates(arr):
    # Create a dictionary to store the count of each number
    num_count = defaultdict(int)
    
    # Count the occurrences of each number in the array
    for num in arr:
        num_count[num] += 1
    
    # Find and collect the numbers with counts greater than 1 (duplicates)
    duplicates = [num for num, count in num_count.items() if count > 1]
    
    return duplicates

# Testcase 1
A = [1, 2, 5, 4, 0]
duplicates_A = find_duplicates(A)
print("Duplicates in Testcase 1:", duplicates_A)

# Testcase 2
B = [1, 2, 3, 4, 5]
duplicates_B = find_duplicates(B)
print("Duplicates in Testcase 2:", duplicates_B)
