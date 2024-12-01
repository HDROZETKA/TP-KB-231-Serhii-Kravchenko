def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'Ділення на нуль заборонено.'
    return a / b


def power(a, b):
    return a ** b


def calculator(a, b, action):
    match action:
        case '1':
            return add(a, b)
        case '2':
            return subtract(a, b)
        case '3':
            return multiply(a, b)
        case '4':
            return divide(a, b)
        case '5':
            return power(a, b)


def input_call():
    print('''Список можливих дій:
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Піднесення до степеня''')
    action = input("Оберіть дію: ")
    if action in ('1', '2', '3', '4', '5'):
        a = float(input("Уведіть число a: "))
        b = float(input("Уведіть число b: "))
        return a, b, action
    else:
        print('Обрано некоректну дію.')


input_data = input_call()
if input_data is not None:
    print(f'\nРезультат: {calculator(input_data[0], input_data[1], input_data[2])}')
