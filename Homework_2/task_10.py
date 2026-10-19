class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма должна быть положительной")

    if amount > balance:
        raise InsufficientFundsError("Недостаточно средств")

    return balance - amount


try:
    balance = float(input("Баланс: "))
    amount = float(input("Сумма снятия: "))

    new_balance = withdraw(balance, amount)
    print("Новый баланс:", new_balance)

except BankError as error:
    print("Ошибка банка:", error)

except ValueError:
    print("Введите корректное число")