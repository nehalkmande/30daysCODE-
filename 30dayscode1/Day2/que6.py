# function to check if a key exists in an array
def key_exists(key, arr):
    return key in arr

# TestCase 1
k = 4
A = [1, 2, 5, 4, 0]

# Check if k exists in array A using the function
if key_exists(k, A):
    print("Key", k, "found in array A")
else:
    print("Key", k, "not found in array A")

# TestCase 2
k = 33
B = [11, 22, 33, 44]

# Check if k exists in array B using the function
if key_exists(k, B):
    print("Key", k, "found in array B")
else:
    print("Key", k, "not found in array B")
