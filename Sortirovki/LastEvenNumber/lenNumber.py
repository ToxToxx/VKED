def first_even_from_end(arr):
    stack = []
    for num in reversed(arr):
        if num % 2 == 0:
            return num
        else:
            stack.append(num)

    return -1

num_elements = int(input())
if num_elements > 0:
    input_array = list(map(int, input().split()))
    result = first_even_from_end(input_array)
    print(result)
else:
    print(-1)