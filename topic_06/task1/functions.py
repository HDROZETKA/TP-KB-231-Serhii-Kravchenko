import logging


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.warning('Користувач намагався поділити на нуль.')
        return 'Ділення на нуль заборонено.'


def power(a, b):
    return a ** b
