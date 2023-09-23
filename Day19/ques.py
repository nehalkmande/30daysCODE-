def partition_negative_numbers(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            # Swap the elements at left and right indices
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Test the function
arr = [-1, -1, 0, 9, -6]
partition_negative_numbers(arr)
print(arr)

#cd 'C:\Users\Nehal M\30dayscode1\Day2\Day3\Day4\Day5\Day6\Day7\Day8\Day10\Day11\Day12\Day19'
