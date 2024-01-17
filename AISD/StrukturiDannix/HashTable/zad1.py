def are_anagrams(input_str):
    words = input_str.split()

    if len(words) != 2:
        print("false")
        return

    frequency_a = {}
    frequency_b = {}

    for char in words[0]:
        frequency_a[char] = frequency_a.get(char, 0) + 1

    for char in words[1]:
        frequency_b[char] = frequency_b.get(char, 0) + 1

    if frequency_a == frequency_b:
        print("true")
    else:
        print("false")
    return

user_input = input()
are_anagrams(user_input)


