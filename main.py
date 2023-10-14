import logging
# import pydantic
from pydantic import BaseModel


class User(BaseModel):
    name: str
    mail: str
    address: str


class Banks(BaseModel):
    bank_name: str
    rating: str
    opened_in: str


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
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
             name = input('введите ваше имя: ')
             mail = input('введите вашу почту: ')
             address = input('введите ваш адресс ')
             bank_name = input('введите название банка которым пользуетесь: ')
             rating = input('введите его рейтинг банка: ')
             opened_in = input('введите дату когда последний раз пользовались услугами банка: ')
             cardholder = User
             which_bank = Banks
             opened_card = input('введите дату регистрации вашей карты: ')
             card = Cards
             amount = int(input('введите ваш счёт: '))
             currency = input('введите вашу валюту: ')

             user = User(name=name,
                         mail=mail,
                         address=address,
                         bank_name=bank_name,
                         rating=rating,
                         opened_in=opened_in,
                         opened_card=opened_card,
                         amount=amount,
                         currency=currency)

             db.append({name:dict(user)})
    #         user = User(name=input('введите имя: '),
    #                     mail=input('введите вашу почту: '),
    #                     address=input('введите ваш адрес: '))
    #         print(user)
    #         db.append(user)
    #
    #         bank = Bakns(bank_name=input('введите название вашего банка: '),
    #                      rating=input('введите рейтинг банка: '),
    #                      opened_in=input('дата вашей регистрации в этом банке: '))
    #         print(bank)
    #         db.append(bank)
    #
    #         card = Cards(cardholder=user,
    #                      which_bank=bank,
    #                      opened_card=input('дата регистрации вашей карты: '))
    #         print(card)
    #         db.append(card)
    #
    #         balance = Balance(card=card,
    #                           ammount=int(input('введите ваш счёт: ')),
    #                           currency=input('введите валюту: '))
    #         print(balance)
    #         db.append(balance)
    #
         except:
            logging.basicConfig(format="%(asctime)s | %(messages)s", filename='errors.log')
            logging.warning('There is a mistake')
            print('ERROR')

    elif z.lower() == 'банковские операции':
        x = input('введите одну из банковых операций: ')

        if x.lower() == 'пополнить баланс':
            c = int(input('введите сумму пополнения: '))

            print(f'Ваш счёт: {calc1(amount, c)}')

        elif x.lower() == 'снять деньги':
            c = int(input('введите суммы снятия: '))

            print(f'Ваш счёт: {calc2(amount, c)}')

        elif x.lower() == 'умножение счёта':
            c = int(input('введите сумму умножения: '))

            print(f'Ваш счёт: {calc3(amount, c)}')

    elif z == 'stop':
        print(db)
        break

