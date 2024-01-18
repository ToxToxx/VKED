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