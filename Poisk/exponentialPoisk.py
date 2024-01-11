def exponential_search(arr, target):
    if not arr:
        return -1, -1

    n = len(arr)

    if arr[0] == target:
        return 0, 1

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    low, high = i // 2, min(i, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return low, mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, -1

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

start, end = exponential_search(arr, target)

if start == -1:
    print("-1")
else:
    print(f"{start} {end}")