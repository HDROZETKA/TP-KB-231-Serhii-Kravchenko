# strip()
string = input("Уведіть строку, де на початку або у кінці будуть цифри, щоб їх вирізати: ")
print(string.strip("1234567890"))  # видаляє будь-які цифри на початку на у кінці

# capitalize()
string = input("Уведіть своє ім'я з малої літери: ")
print(string.capitalize())

# title()
string = input("Уведіть своє повне ПІБ з малої літери: ")
print(string.title())

# lower()
string = input("Уведіть будь-що капсом(кожна бувква велика): ")
print(string.lower())

# upper()
string = input("Уведіть будь-що де кожна буква маленька: ")
print(string.upper())
