def find_min_max_multiply(arr):
    min_element = float('inf')  # Инициализация переменной для хранения минимального элемента
    for i in range(len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]  # Обновление минимального элемента, если текущий элемент меньше

    max_element = float('-inf')  # Инициализация переменной для хранения максимального элемента
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]  # Обновление максимального элемента, если текущий элемент больше

    return min_element * max_element  # Возвращаем произведение минимального и максимального элементов

# Ввод данных
n = int(input())  # Количество элементов в массиве
array = list(map(int, input().split()))  # Ввод массива чисел

# Находим и выводим результат умножения минимального и максимального элементов
result = find_min_max_multiply(array)
print(result)
