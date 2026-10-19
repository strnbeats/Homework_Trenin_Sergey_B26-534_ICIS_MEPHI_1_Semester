with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = []
    errors = []

    for line_number, line in enumerate(file, start=1):
        try:
            numbers.append(int(line.strip()))
        except ValueError:
            errors.append(line_number)

with open("result.txt", "w", encoding="utf-8") as file:
    if numbers:
        file.write(f"Минимум: {min(numbers)}\n")
        file.write(f"Максимум: {max(numbers)}\n")
        file.write(f"Среднее: {sum(numbers) / len(numbers)}\n")
    else:
        file.write("Чисел нет\n")

    if errors:
        file.write(f"Ошибочные строки: {errors}\n")

print("Результаты сохранены в result.txt")