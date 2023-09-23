def find_all_subarrays(arr):
    subarrays = []

    for start in range(len(arr)):
        for end in range(start, len(arr)):
            subarray = arr[start:end + 1]
            subarrays.append(subarray)

    return subarrays

arr = [1, 2, 3]
subarrays = find_all_subarrays(arr)
print(subarrays)
