def find_min_element(arr):
    current_index = 0  # Инициализация текущего индекса

    # Пока у текущего узла есть левый потомок
    while 2 * current_index + 1 < len(arr):
        current_index = 2 * current_index + 1  # Переходим к левому потомку

    return arr[current_index]  # Возвращаем минимальный элемент в поддереве

# Ввод данных
array_capacity = int(input())  # Вводим количество элементов в массиве
numbers_array = list(map(int, input().split()))  # Вводим массив чисел

# Находим и выводим минимальный элемент
min_element = find_min_element(numbers_array)
print(min_element)
