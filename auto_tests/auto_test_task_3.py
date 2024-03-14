import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


# Введите ваше решение ниже
def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False


def deposit(amount):
    if check_multiplicity(amount):
        global bank_account
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    global bank_account
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
    perc = 0
    if amount * PERCENT_REMOVAL < MIN_REMOVAL:
        perc = MIN_REMOVAL
    elif amount * PERCENT_REMOVAL > MAX_REMOVAL:
        perc = MAX_REMOVAL
    else:
        perc = amount * PERCENT_REMOVAL
    res = amount + perc
    if res > bank_account:
        operations.append(f'Недостаточно средств. Сумма с комиссией {int(res)} у.е. На карте {bank_account} у.е.')
    else:
        bank_account = bank_account - res
        operations.append(
            f'Снятие с карты {int(amount)} у.е. Процент за снятие {int(perc)} у.е.. Итого {int(bank_account)} у.е.')


def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        res_sum = bank_account * RICHNESS_PERCENT
        bank_account = bank_account - res_sum
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {res_sum} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

# REMOVALотправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# deposit(1_000_000_000_000_000)
# deposit(10_000)
# deposit(1000)
# withdraw(4000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# deposit(173)
# withdraw(21)
# exit()

# print(operations)