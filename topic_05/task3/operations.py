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
