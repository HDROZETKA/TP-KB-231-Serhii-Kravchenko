class Student:
    def __init__(self, name, phone, age, sex):
        self.name = name
        self.phone = phone
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f"Student(name={self.name}, phone={self.phone}, age={self.age}, sex={self.sex})"
