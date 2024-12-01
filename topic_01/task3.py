def find_discriminator(a, b, c):
    return b ** 2 - 4 * a * c


def input_call():
    a = int(input("Уведіть a: "))
    b = int(input("Уведіть b: "))
    c = int(input("Уведіть c: "))
    return a, b, c


coeffs = input_call()

print(f'\nПри таких коефіцієнтах Дискримінант буде: {find_discriminator(coeffs[0], coeffs[1], coeffs[2])}')
