def max_product_memoization(nums, k, index, remaining, memo):
    """
    Рекурсивная функция с мемоизацией для вычисления максимального произведения подпоследовательности.
    
    :param nums: Исходный массив чисел
    :param k: Количество элементов в подпоследовательности
    :param index: Текущий индекс в массиве
    :param remaining: Сколько еще элементов нужно выбрать
    :param memo: Словарь для хранения результатов вычислений
    :return: Максимальное произведение подпоследовательности
    """
    # Базовый случай: если необходимо выбрать 0 элементов или дошли до конца массива
    if remaining == 0 or index >= len(nums):
        return 1

    # Проверяем, есть ли результат в мемоизированном словаре
    if (index, remaining) in memo:
        return memo[(index, remaining)]

    # Включаем текущий элемент в подпоследовательность
    include_current = nums[index] * max_product_memoization(nums, k, index + 1, remaining - 1, memo)
    
    # Пропускаем текущий элемент
    exclude_current = max_product_memoization(nums, k, index + 1, remaining, memo)

    # Выбираем максимальное произведение
    result = max(include_current, exclude_current)
    
    # Сохраняем результат в мемоизированный словарь
    memo[(index, remaining)] = result

    return result

def max_product(nums, k):
    """
    Функция для нахождения максимального произведения подпоследовательности.
    
    :param nums: Исходный массив чисел
    :param k: Количество элементов в подпоследовательности
    :return: Максимальное произведение подпоследовательности
    """
    # Если массив пуст или требуется выбрать 0 элементов, возвращаем 0
    if not nums or k == 0:
        return 0

    # Определяем effective_k, чтобы избежать выхода за границы массива
    effective_k = min(k, len(nums))
    
    # Инициализируем словарь для мемоизации результатов
    memo = {}
    
    # Вызываем вспомогательную функцию для рекурсивного вычисления
    return max_product_memoization(nums, effective_k, 0, effective_k, memo)

# Ввод данных
n = int(input())  # Количество элементов в массиве
nums = list(map(int, input().split()))  # Ввод массива чисел
k = int(input())  # Количество элементов в подпоследовательности

# Вызываем функцию и выводим результат
result = max_product(nums, k)
print(result)
