from student_list import StudentList
from student import Student
from file_handler import load_students, save_students


def main():
    group = StudentList()
    group.students = load_students('students.csv')

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case 'C' | 'c':
                name = input("Enter student name: ")
                phone = input("Enter student phone: ")
                age = int(input("Enter student age: "))
                sex = input("Enter student sex (M/F): ")
                group.add_student(Student(name, phone, age, sex))
                print("Student added.")
            case 'U' | 'u':
                name = input("Enter the name of the student to update: ")
                phone = input("Enter new phone (leave empty to keep current): ")
                age = input("Enter new age (leave empty to keep current): ")
                sex = input("Enter new sex (leave empty to keep current): ")
                group.update_student(name, phone or None, int(age) if age else None, sex or None)
                print("Student updated.")
            case 'D' | 'd':
                name = input("Enter the name of the student to delete: ")
                group.delete_student(name)
                print("Student deleted.")
            case 'P' | 'p':
                print(group)
            case 'X' | 'x':
                save_students('students.csv', group.students)
                print("Exiting and saving data...")
                break
            case _:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
