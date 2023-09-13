A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

common_elements = list(set(A) & set(B))
print("Common Elements:", common_elements)


A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

sum_A = sum(A)
sum_B = sum(B)

if sum_A > sum_B:
    result_array = A
    print("Array A has a bigger sum:", sum_A)
else:
    result_array = B
    print("Array B has a bigger sum:", sum_B)

print("Result Array:", result_array)


A = [1, 2, 5, 4, 0]
B = [1, 2, 3, 4, 5]

merged_array = A + B
merged_array.sort()  # Sort the merged array

middle_index = len(merged_array) // 2
middle_element = merged_array[middle_index]

print("Middle Element of Merged Array:", middle_element)
