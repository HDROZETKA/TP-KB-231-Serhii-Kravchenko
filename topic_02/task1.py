
def find_discriminator(a, b, c):
    return b ** 2 - 4 * a * c

def find_roots(a, b, c):
    d = find_discriminator(a, b, c)
    if d < 0:
        return None
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


def input_call():
    a = int(input("Уведіть a: "))
    b = int(input("Уведіть b: "))
    c = int(input("Уведіть c: "))
    return a, b, c


coeffs = input_call()
answer = find_roots(coeffs[0], coeffs[1], coeffs[2])

print()
if answer is None:
    print('Коренів не знайдено оскільки Дискримінант від\'ємний.')
else:
    print('Корені квадратного рівняння: ', answer)
