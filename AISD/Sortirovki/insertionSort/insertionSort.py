list_capacity = int(input())
numbers_list = list(map(int, input().split()))

for i in range(1, list_capacity):
    key = numbers_list[i]
    j = i - 1
    while j >= 0 and numbers_list[j] > key:
        numbers_list[j+1] = numbers_list[j]
        j = j - 1
    numbers_list[j+1] = key

print(" ".join(str,numbers_list))
