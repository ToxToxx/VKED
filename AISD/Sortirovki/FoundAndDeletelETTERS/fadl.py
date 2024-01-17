def delete_letters(s):
    stack = []
    for letter in s:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)

foundable_line = input()
result = delete_letters(foundable_line)
print(result)

