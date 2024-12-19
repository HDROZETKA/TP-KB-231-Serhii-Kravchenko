# Функція для визначення пріоритету операторів
def get_priority(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


# Функція для перевірки, чи є символ оператором
def is_operator(c):
    return c in ('+', '-', '*', '/', '^')


# Перетворення інфіксного запису у ЗПН (зворотний польський запис)
def infix_to_rpn(expression):
    output = []
    stack = []

    for token in tokenize(expression):
        if token.isdigit() or is_float(token):
            output.append(token)  # Операнди одразу додаємо до виходу
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Видаляємо '(' зі стеку
        elif is_operator(token):
            while stack and get_priority(stack[-1]) >= get_priority(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


# Обчислення виразу у ЗПН
def evaluate_rpn(rpn):
    stack = []

    for token in rpn:
        if token.isdigit() or is_float(token):
            stack.append(float(token))
        elif is_operator(token):
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]


# Розбиття вхідного рядка на токени
def tokenize(expression):
    tokens = []
    number = ''
    for c in expression:
        if c.isdigit() or c == '.':
            number += c
        else:
            if number:
                tokens.append(number)
                number = ''
            if c.strip():  # Пропускаємо пробіли
                tokens.append(c)
    if number:
        tokens.append(number)
    return tokens


# Перевірка, чи є число дійсним числом
def is_float(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


# Головна функція
if __name__ == "__main__":
    expr = input("Введіть математичний вираз: ")
    try:
        rpn = infix_to_rpn(expr)
        print("ЗПН:", ' '.join(rpn))
        result = evaluate_rpn(rpn)
        print("Результат:", result)
    except Exception as e:
        print("Помилка:", str(e))
