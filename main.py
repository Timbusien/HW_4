import logging
# import pydantic
from pydantic import BaseModel


class User(BaseModel):
    name: str
    mail: str
    address: str


class Bakns(BaseModel):
    bank_name: str
    rating: str
    opened_in: str


class Cards(BaseModel):
    cardholder: User
    which_bank: Bakns
    opened_card: str


class Balance(BaseModel):
    card: Cards
    amount: int = 0
    currency: str


db = []


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
    if z.lower() == 'заполнение':

        try:
            user = User(name=input('введите имя: '),
                        mail=input('введите вашу почту: '),
                        address=input('введите ваш адрес: '))
            print(user)
            db.append(user)

            bank = Bakns(bank_name=input('введите название вашего банка: '),
                         rating=input('введите рейтинг банка: '),
                         opened_in=input('дата вашей регистрации в этом банке: '))
            print(bank)
            db.append(bank)

            card = Cards(cardholder=user,
                         which_bank=bank,
                         opened_card=input('дата регистрации вашей карты: '))
            print(card)
            db.append(card)

            balance = Balance(card=card,
                              ammount=int(input('введите ваш счёт: ')),
                              currency=input('введите валюту: '))
            print(balance)
            db.append(balance)

        except:
            logging.basicConfig(format="%(asctime)s | %(messages)s", filename='errors.log')
            logging.warning('There is a mistake')
            print('ERROR')

    elif z.lower() == 'банковские операции':
        x = input('введите одну из банковых операций: ')

        if x.lower() == 'пополнить баланс':
            c = int(input('введите сумму пополнения: '))

            print(f'Ваш счёт :{calc1(balance.amount, c)}')

        elif x.lower() == 'снять деньги':
            c = int(input('введите суммы снятия: '))

            print(f'Ваш счёт :{calc2(balance.amount, c)}')

        elif x.lower() == 'умножение счёта':
            c = int(input('введите сумму умножения: '))

            print(f'Ваш счёт : {calc3(balance.amount, c)}')

    elif z == 'stop':
        print(db)
        break

)