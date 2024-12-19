from student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda s: s.name)

    def delete_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, age=None, sex=None):
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if age:
                    student.age = age
                if sex:
                    student.sex = sex
                self.students.sort(key=lambda s: s.name)
                return

    def __repr__(self):
        return "\n".join(str(s) for s in self.students)
