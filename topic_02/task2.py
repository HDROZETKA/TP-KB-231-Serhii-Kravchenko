def calculator_if(a, b, action):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b


def calculator_match(a, b, action):
    match action:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b


a_str = input("Уведіть число a: ")
b_str = input("Уведіть число b: ")
action_str = input("Уведіть дію(+, -, *, /): ")

print(f'\nОтримане число за допомогою if калькулятора: ', calculator_if(int(a_str), int(b_str), action_str))
print(f'\nОтримане число за допомогою match калькулятора: ', calculator_match(int(a_str), int(b_str), action_str))
