def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))

# Input from user
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

print("Largest element is:", find_max(arr, n))
