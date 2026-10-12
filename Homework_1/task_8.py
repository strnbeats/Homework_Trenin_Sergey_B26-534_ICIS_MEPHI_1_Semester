import functools


class CallLimitError(Exception):
    pass


def limit_calls(limit):
    def decorator(func):
        calls = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= limit:
                raise CallLimitError("Функция " + func.__name__ + " уже вызвана " + str(limit) + " раз(а)")
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


def limit_calls_value(limit, special_value=None):
    def decorator(func):
        calls = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= limit:
                return special_value
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_calls(3)
def hello():
    """Печатает приветствие"""
    print("Hello")


@limit_calls(2)
def add(a, b=0):
    return a + b


@limit_calls(2)
def another():
    return "another"


@limit_calls_value(2, "лимит исчерпан")
def square(x):
    return x * x


print("Функция hello, лимит 3")
for i in range(5):
    try:
        hello()
    except CallLimitError as error:
        print("Ошибка:", error)

print()
print("Функция add с аргументами, лимит 2")
print(add(2, 3))
print(add(10, b=5))
try:
    print(add(1, 1))
except CallLimitError as error:
    print("Ошибка:", error)

print()
print("Счетчики независимы:", another(), another())
try:
    another()
except CallLimitError as error:
    print("Ошибка:", error)

print()
print("Вариант со специальным значением, лимит 2")
for i in range(1, 5):
    print(square(i))

print()
print("Метаданные сохранены:", hello.__name__, "|", hello.__doc__)