import logging
from operations import InputHandler
from functions import Calculator

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("Програму було запущено.")
    print('Калькулятор розпочав свою роботу.\n\n')

    calculator = Calculator()
    input_handler = InputHandler()

    while True:
        input_data = input_handler.get_input()
        if input_data is not None:
            a, b, action = input_data
            result = calculator.perform_operation(a, b, action)
            print(f'\nРезультат: {result}\n')


if __name__ == "__main__":
    main()
