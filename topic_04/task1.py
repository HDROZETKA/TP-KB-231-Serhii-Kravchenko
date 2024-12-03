def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ділення на нуль заборонено.'


def power(a, b):
    return a ** b


def calculator(a, b, action):
    if action == '1':
        return add(a, b)
    elif action == '2':
        return subtract(a, b)
    elif action == '3':
        return multiply(a, b)
    elif action == '4':
        return divide(a, b)
    elif action == '5':
        return power(a, b)


def input_call():
    print('''Список можливих дій:
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Піднесення до степеня''')
    action = input("\nОберіть дію або введіть 'exit' для виходу: ").strip().lower()
    if action in ('1', '2', '3', '4', '5'):
        try:
            a = float(input("\nУведіть число a: "))
            b = float(input("Уведіть число b: "))
            return a, b, action
        except ValueError:
            print('\nВи неправильно ввели число. У якості роздільника використовується крапка.\n')
    elif action == 'exit':
        print('\n\n\nКалькулятор припинив свою роботу.')
        exit()
    else:
        print('\nОбрано некоректну дію.\n')


print('Калькулятор розпочав свою роботу.\n\n')
while True:
    input_data = input_call()
    if input_data is not None:
        print(f'\nРезультат: {calculator(input_data[0], input_data[1], input_data[2])}\n')
