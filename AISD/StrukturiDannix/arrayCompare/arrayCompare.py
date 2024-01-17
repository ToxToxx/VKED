"""array_capacity = int(input())
numbers_to_compare = list(map(int, input().split()))
element = int(input())
compare_counter = 0

for num in numbers_to_compare:
    if num != element:
        compare_counter += 1

print(compare_counter)"""

array_capacity = int(input())
grades_list = list(map(int, input().split()))

zeros_list = [grade for grade in grades_list if grade == 0]
non_zeros_list = [grade for grade in grades_list if grade != 0]

result_list = non_zeros_list + zeros_list

print(" ".join(map(str, result_list)))
