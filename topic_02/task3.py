def calculator(a, b, action):
    match action:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
        case 5:
            return a ** b
        case _:
            return 'Уведено некоректну дію.'


def input_call():
    a = float(input("Уведіть число a: "))
    b = float(input("Уведіть число b: "))
    print('''
Список можливих дій:
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Возведення до степеня''')
    action = input("Виберіть дію: ")
    return a, b, action


input_data = input_call()

print(f'\nРезультат: {calculator(input_data[0], input_data[1], input_data[2])}')
