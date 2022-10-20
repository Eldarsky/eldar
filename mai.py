import os
from envparse import env
from casino_logic import bet
env.read_envfile('settings.env')
balance = int(os.getenv('MY_MONEY'))
while True:
    command = input('Будете играть?')
    if command == 'нет':
        print(f'У вас на балане осталось {balance}')
        break
    rate = int(input('введите число для ставки'))
    amount = int(input('Введите сумму для ставки '))
    if rate < 1 or rate > 30:
        print('Неправильное число для ставки')
        continue
    if amount > balance:
        print('Неправильная сумма для ставки')
        continue
    balance = bet(rate, amount, balance)