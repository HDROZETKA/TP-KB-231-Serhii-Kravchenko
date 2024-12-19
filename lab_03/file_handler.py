import csv
from student import Student


def load_students(filename):
    students = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(Student(row['name'], row['phone'], int(row['age']), row['sex']))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return students


def save_students(filename, students):
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['name', 'phone', 'age', 'sex']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    'name': student.name,
                    'phone': student.phone,
                    'age': student.age,
                    'sex': student.sex
                })
    except Exception as e:
        print(f"Error saving to file: {e}")
