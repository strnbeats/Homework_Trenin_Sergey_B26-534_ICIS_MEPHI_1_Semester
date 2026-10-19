from pathlib import Path

path = Path(input("Файл с числами: "))

total = 0
count = 0
minimum = None
maximum = None

try:
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            try:
                number = int(line.strip())
            except ValueError:
                continue

            total += number
            count += 1

            if minimum is None or number < minimum:
                minimum = number

            if maximum is None or number > maximum:
                maximum = number

    if count:
        print("Сумма:", total)
        print("Минимум:", minimum)
        print("Максимум:", maximum)
        print("Количество:", count)
        print("Среднее:", total / count)
    else:
        print("Чисел нет")

except OSError as error:
    print("Ошибка чтения файла:", error)