from functools import reduce

# Map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Destructuring
point = (3, 4)
x, y = point

# Ternary Operator
age = 25
status = "Adult" if age >= 18 else "Minor"

# Spread Operator (Equivalent in Python)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]

# Printing results
print("Mapped Numbers:", squared_numbers)
print("Filtered Even Numbers:", even_numbers)
print("Sum of Numbers:", sum_of_numbers)
print("Destructured Point - x:", x, "y:", y)
print("Age Status:", status)
print("Combined List (Equivalent of Spread Operator):", combined_list)

#cd "C:\Users\Nehal M\30dayscode1\Day2\Day3\Day4\Day5\Day6\Day7\Day8\Day10"