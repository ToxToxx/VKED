def rearrange_even_numbers(arr):
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    return arr

n = int(input())
array = list(map(int, input().split()))

result_array = rearrange_even_numbers(array)

print(" ".join(map(str, result_array)))