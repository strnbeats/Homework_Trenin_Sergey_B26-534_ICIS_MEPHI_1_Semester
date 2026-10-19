def parse_number(value):
    return float(value)


try:
    value = input("Введите число: ")
    number = parse_number(value)
    print("Результат:", number)

except ValueError:
    print("Ошибка: введено некорректное число")