import logging

from functions import *
from operations import input_call


logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


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


def start_calc():
    print('Калькулятор розпочав свою роботу.\n\n')
    while True:
        input_data = input_call()
        if input_data is not None:
            print(f'\nРезультат: {calculator(input_data[0], input_data[1], input_data[2])}\n')


if __name__ == "__main__":
    logging.info("Програму було запущено.")
    start_calc()
