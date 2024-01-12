def find_min_element(arr):
    while 2 * current_index + 1 < len(arr):
        current_index = 2 * current_index + 1

    return arr[current_index]

array_capacity = int(input())
numbers_array = list(map(int, input().split()))


min_element = min(numbers_array)

print(min_element)