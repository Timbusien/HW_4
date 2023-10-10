import logging


def calc1(a: int, b: int) -> dict:
    try:
        return a + b
    except TypeError:
        logging.basicConfig(format="%(asctime)s | %(messages)s", filename='errors.log')
        logging.warning('There is a mistake')


def calc2(a: int, b: int) -> dict:
    try:
        return a - b
    except TypeError:
        logging.basicConfig(format="%(asctime)s | %(messages)s", filename='errors.log')
        logging.warning('There is a mistake')


def calc3(a: int, b: int) -> dict:
    try:
        return a * b
    except TypeError:
        logging.basicConfig(format="%(asctime)s | %(messages)s", filename='errors.log')
        logging.warning('There is a mistake')


while True:
    z = input('Введите опцию: ')
    if z == 'c1':
        print(calc1(a = input('число 1: '), b = input('число 2: ')))

    elif z == 'c2':
        print(calc2(a = input('число 1: '), b = input('число 2: ')))

    elif z == 'c3':
        print(calc3(a = input('число 1: '), b = input('число 2: ')))