#так пишутся комментарии
#вывод данных
print("abc")

#динамическая типизация
width = 20
height = 5.75
s = width / height
print(s)

#экранирование
print('''"hello"''')
print("\'hello\'")

#конкатенация
print("hi" + "mark")

#форматирование
print("Hello {}, {}".format("Naruto", 5))
print("{1}, {0}, {2}".format(1,2,3))

#if и инпут
a = int(input("Введи число для if: "))
print("if else", end = " ")
if a == 1:
    print("Hello")
elif a > 3:
    print("Darova")
else:
    print("Bye")

#while 
a = 1
while a <= 3:
    print("While ", a, end = " ")
    a += 1

print()
#for
for i in range(3):
    print(i, end = " for ")

print()
#модель данных
#изменяемые типы - списки, множества и словари (по сути ссылочные типы)
#неизменяемые - объект больше не именяется, всё остальное

#списки
print("             СПИСКИ              ")
a = [3, 5, 1, 10, 13, 12 ,8, 9, 100]
print(a[2])
print(a[-1])
print(a[1:6])
a.append(12)
print(a)
a.insert(1, 300)
print(a)
a.pop()
a.pop(7)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.count(10))
a.clear()
print(a)
a = [str(i) + "k" for i in range(10) if i % 2 == 0]
print(a)

#кортежи - неизменяемы и быстры
print("             Кортежи             ")
b = (1, 2, 3)
print(b)

#множества - набор уникальный элементов в случайном порядке
print("             Сеты             ")
c = {1, 3, 5 ,6}
d = {1, 6 , 4, 2}
print(c & d)

#словари
print("             Словари             ")
e = {1 : "Russia", 2 : "Kazahstan"}
print(e.keys())
print(e.values())

#функции
print("             Функция             ")
def add(x,y):
    return x + y

print(add(2,3))

def returnArgs(*args):
    return args

print(returnArgs("a", 12, 12.03, "PRIVET", 2 + 2))

def returnKwargs(**kwargs):
    return kwargs

print(returnKwargs(a = 1, c = 3, g = 4))