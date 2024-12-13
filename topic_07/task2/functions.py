import logging


class Calculator:
    def perform_operation(self, a, b, action):
        if action == '1':
            return self.add(a, b)
        elif action == '2':
            return self.subtract(a, b)
        elif action == '3':
            return self.multiply(a, b)
        elif action == '4':
            return self.divide(a, b)
        elif action == '5':
            return self.power(a, b)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            logging.warning('Користувач намагався поділити на нуль.')
            return 'Ділення на нуль заборонено.'

    @staticmethod
    def power(a, b):
        return a ** b
