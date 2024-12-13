students = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "sex": "M"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "sex": "F"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "sex": "M"},
    {"name": "Zak", "phone": "0631234567", "age": 23, "sex": "M"}
]


def printAllList():
    for elem in students:
        strForPrint = (
            f"Student name: {elem['name']}, Phone: {elem['phone']}, "
            f"Age: {elem['age']}, Sex: {elem['sex']}"
        )
        print(strForPrint)
    return


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = int(input("Please enter student age: "))
    sex = input("Please enter student sex (M/F): ")
    newItem = {"name": name, "phone": phone, "age": age, "sex": sex}

    # find insert position
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print(f"Element with name {name} has been deleted")
    return


def updateElement():
    name = input("Please enter the name of the student to update: ")
    for item in students:
        if item["name"] == name:
            print(f"Current data: {item}")
            item["phone"] = input(f"Enter new phone (current: {item['phone']}): ") or item["phone"]
            item["age"] = int(input(f"Enter new age (current: {item['age']}): ") or item["age"])
            item["sex"] = input(f"Enter new sex (M/F, current: {item['sex']}): ") or item["sex"]

            # Ensure the list remains sorted
            students.sort(key=lambda x: x["name"])
            print("Student information has been updated.")
            return
    print("Student not found.")


def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                print("Exiting...")
                break
            case _:
                print("Wrong choice. Please try again.")


main()
