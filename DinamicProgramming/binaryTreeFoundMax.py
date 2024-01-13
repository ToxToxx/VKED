class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def array_to_bst(arr, start, end):
    """
    Функция преобразует отсортированный массив в бинарное дерево поиска (BST).

    Parameters:
    - arr: Отсортированный массив.
    - start: Начальный индекс для текущего поддерева.
    - end: Конечный индекс для текущего поддерева.

    Returns:
    - TreeNode: Корень построенного бинарного дерева.
    """
    if start > end:
        return None

    mid = (start + end) // 2
    node = TreeNode(arr[mid])

    node.left = array_to_bst(arr, start, mid - 1)
    node.right = array_to_bst(arr, mid + 1, end)

    return node

def find_max_element(root):
    """
    Функция находит максимальный элемент в бинарном дереве.

    Parameters:
    - root: Корень бинарного дерева.

    Returns:
    - int: Максимальный элемент в бинарном дереве.
    """
    while root.right:
        root = root.right
    return root.value

def find_max_in_bst(arr):
    """
    Функция находит максимальный элемент в бинарном дереве поиска (BST),
    построенном на основе отсортированного массива.

    Parameters:
    - arr: Неотсортированный массив.

    Returns:
    - int: Максимальный элемент в бинарном дереве.
    """
    arr.sort()  # Сортируем массив перед построением бинарного дерева
    n = len(arr)
    root = array_to_bst(arr, 0, n - 1)
    max_element = find_max_element(root)
    return max_element

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вычисление и вывод результата
result = find_max_in_bst(arr)
print(result)



result = find_max_in_bst(arr)
print(result)
