class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент {self.name}, йому {self.age} років"


# Створення списку студентів
students = [
    Student("Вася", 21),
    Student("Коля", 20),
    Student("Петя", 19),
    Student("Серж", 18)
]

# Сортування за віком (lambda-функція як ключ)
sorted_students = sorted(students, key=lambda student_key: student_key.age)

# Виведення відсортованого списку
for student in sorted_students:
    print(student)
