string = input("Уведіть будь-що щоб його обернути в зворотному порядку за допомогою слайсингу: ")

print(f'\nПочатковий вигляд вашого вводу: {string}')
print(f'У зворотному напрямі за допомогою слайсингу: {string[::-1]}')

reversed_text = "".join(reversed(string))
print(f'У зворотному напрямі за допомогою слайсингу: {reversed_text}')

reversed_text = ""
for char in string:
    reversed_text = char + reversed_text
print(f'У зворотному напрямі за допомогою циклу: {reversed_text}')
