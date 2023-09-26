from collections import Counter

def find_majority_element(nums):
    # Count the occurrences of each element in the list
    counts = Counter(nums)
    
    # Calculate n/2
    n = len(nums)
    half_n = n // 2
    
    # Find the element with n/2 occurrences
    for num, count in counts.items():
        if count == half_n:
            return num

# Example usage:
nums = [1, 2, 2, 2, 1]
result = find_majority_element(nums)
print("Element with n/2 occurrences:", result)
