def max_repeating_char_count(input_str):
    char_frequency = {}

    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    max_count = max(char_frequency.values(), default=0)

    return max_count

input_str = input()
result = max_repeating_char_count(input_str)
print(result)