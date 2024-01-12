def find_min_max_multiply(arr):
    min_element = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]

    max_element = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return min_element * max_element

n = int(input())
array = list(map(int, input().split()))

result = find_min_max_multiply(array)

print(result)
