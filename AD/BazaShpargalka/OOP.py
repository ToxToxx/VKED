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