A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]

# Convert both arrays to sets
set_A = set(A)
set_B = set(B)

# Check for duplicates by finding the intersection of the sets
duplicates = set_A.intersection(set_B)

if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")

  #  cd "C:\Users\Nehal M\30dayscode1\Day2\Day3"
