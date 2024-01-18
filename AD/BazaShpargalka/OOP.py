#СОЗДАНИЕ КЛАССА
class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group
    
    def printStudentInfo(self):
        print(f"Имя студента: {self.name}, Возраст: {self.age}, Группа: {self.group}")

student1 = Student("Алексей", 21, "ПИ-19Г")
student2 = Student("Олег", 20, "ПИ-20Г")

student1.printStudentInfo()
student2.printStudentInfo()

#Наследование
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def dealDamage(self):
        pass

class Knife(Weapon):
    def dealDamage(self):
        return f"{self.name} наносит {self.damage} урона и {self.damage} урона кровотечением"
    
class Hammer(Weapon):
    def dealDamage(self):
        return f"{self.name} наносит {self.damage} дробящего урона"
    
hammer = Hammer("Bullhammer", 25)
knife = Knife("Zatochka", 5)

print(hammer.dealDamage())
print(knife.dealDamage())

#Инкапсуляция
class Circle:
    def __init__(self, radius):
        self.__radius = radius #двойное подчеркивание для инкапсуляции

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, new_radius):
        if new_radius >= 0:
            self.__radius = new_radius
    
    def area(self):
        return 3.14159 * self.__radius ** 2

circle = Circle(5)

#использование геттера и сеттера
print(circle.get_radius())
print(f"Площадь круга: {circle.area()}")

circle.set_radius(10)
print(circle.get_radius())
print(f"Площадь круга: {circle.area()}")


#Полиморфизм
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} это Собака"

class Bear(Animal):
    def speak(self):
        return f"{self.name} это Медведь"
    
class Bull(Animal):
    def speak(self):
        return f"{self.name} это Бык"
    
animals = [Dog("Шарик"), Bear("Миша"), Bull("Кексик")]

for animal in animals:
    print(animal.speak())

