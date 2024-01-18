#ПРИМЕР ИСПОЛЬЗОВАНИЯ ФУНКЦИИ ВЫСШЕГО ПОРЯДКА

def apply_operation(operation, x, y):
    return operation(x,y)

#функции, которые как аргументы
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На ноль делить нельзя"
    
result1 = apply_operation(add, 5, 4)
result2 = apply_operation(substract, 654, 213)
result3 = apply_operation(multiply, 17, 1234)
result4 = apply_operation(divide, 1238, 64)

print(f"Сложение: {result1}")
print(f"Вычитание: {result2}")
print(f"Умножение: {result3}")
print(f"Деление: {result4}")
