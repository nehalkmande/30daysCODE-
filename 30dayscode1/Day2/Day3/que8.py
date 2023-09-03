#Occurrence of key in an array
key = 1
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# occurrences of key in array A
count_in_A = A.count(key)

# occurrences of key in array B
count_in_B = B.count(key)

# Total occurrences in both arrays
total_occurrences = count_in_A + count_in_B

print(f"The key {key} occurs {total_occurrences} times in the arrays.")
