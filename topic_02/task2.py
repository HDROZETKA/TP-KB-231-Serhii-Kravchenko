def calculator(a, b, action):
    if action == 1:
        return a + b
    elif action == 2:
        return a - b
    elif action == 3:
        return a * b
    elif action == 4:
        return a / b
    elif action == 5:
        return a ** b
    else:
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
