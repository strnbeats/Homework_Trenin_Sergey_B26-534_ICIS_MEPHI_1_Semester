import random


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
EXPENSE_CATEGORIES = ["food", "transport", "rent", "entertainment", "health", "clothes", "internet"]
INCOME_CATEGORIES = ["salary", "bonus", "freelance"]


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def is_valid_date(date):
    parts = date.split("-")
    if len(parts) != 3:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    if month < 1 or month > 12:
        return False
    max_day = DAYS_IN_MONTH[month - 1]
    if month == 2 and is_leap_year(year):
        max_day = 29
    if day < 1 or day > max_day:
        return False
    return True


def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 4:
        return None
    date = parts[0].strip()
    category = parts[1].strip()
    kind = parts[3].strip().lower()
    if not is_valid_date(date):
        return None
    if category == "":
        return None
    if kind != "income" and kind != "expense":
        return None
    try:
        amount = float(parts[2])
    except ValueError:
        return None
    if amount <= 0:
        return None
    return date, category, amount, kind


def analyze_finances(path):
    total_income = 0
    total_expense = 0
    expense_by_category = {}
    expense_by_month = {}
    biggest_expense = None
    valid_count = 0
    with open(path, "r", encoding="utf-8") as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                if line.strip().lower().startswith("date"):
                    continue
            if line.strip() == "":
                continue
            record = parse_line(line)
            if record is None:
                continue
            date, category, amount, kind = record
            valid_count += 1
            if kind == "income":
                total_income += amount
            else:
                total_expense += amount
                if category in expense_by_category:
                    expense_by_category[category] += amount
                else:
                    expense_by_category[category] = amount
                month = date[:7]
                if month in expense_by_month:
                    expense_by_month[month] += amount
                else:
                    expense_by_month[month] = amount
                if biggest_expense is None or amount > biggest_expense[2]:
                    biggest_expense = (date, category, amount)
    if valid_count == 0:
        return None
    top_category = None
    for category in expense_by_category:
        if top_category is None or expense_by_category[category] > expense_by_category[top_category]:
            top_category = category
    top_month = None
    for month in expense_by_month:
        if top_month is None or expense_by_month[month] > expense_by_month[top_month]:
            top_month = month
    return {
        "income": total_income,
        "expense": total_expense,
        "difference": total_income - total_expense,
        "top_category": top_category,
        "top_category_sum": expense_by_category.get(top_category),
        "biggest_expense": biggest_expense,
        "top_month": top_month,
        "top_month_sum": expense_by_month.get(top_month),
        "valid_records": valid_count,
    }


def random_date():
    month = random.randint(1, 12)
    day = random.randint(1, DAYS_IN_MONTH[month - 1])
    return "2026-" + str(month).zfill(2) + "-" + str(day).zfill(2)


def generate_file(path, count=5000, bad_lines=30):
    if count < 1000:
        count = 1000
    with open(path, "w", encoding="utf-8") as file:
        file.write("date,category,amount,type\n")
        for i in range(count):
            date = random_date()
            if random.random() < 0.1:
                category = random.choice(INCOME_CATEGORIES)
                amount = random.randint(30000, 150000)
                kind = "income"
            else:
                category = random.choice(EXPENSE_CATEGORIES)
                amount = random.randint(100, 15000)
                kind = "expense"
            file.write(date + "," + category + "," + str(amount) + "," + kind + "\n")
        for i in range(bad_lines):
            variant = i % 5
            if variant == 0:
                file.write("2026-13-45,food,500,expense\n")
            elif variant == 1:
                file.write("2026-05-05,food,abc,expense\n")
            elif variant == 2:
                file.write("2026-05-05,food,500\n")
            elif variant == 3:
                file.write("2026-05-05,food,-100,expense\n")
            else:
                file.write("2026-05-05,food,500,gift\n")


def print_result(result):
    if result is None:
        print("Нет корректных данных")
        return
    print("Корректных записей:", result["valid_records"])
    print("Общая сумма доходов:", result["income"])
    print("Общая сумма расходов:", result["expense"])
    print("Разница доходов и расходов:", result["difference"])
    print("Категория с наибольшими расходами:", result["top_category"], result["top_category_sum"])
    print("Самый большой расход:", result["biggest_expense"])
    print("Месяц с наибольшими расходами:", result["top_month"], result["top_month_sum"])


def write_small_file(path):
    lines = [
        "date,category,amount,type",
        "2026-01-01,food,1500,expense",
        "2026-01-02,salary,100000,income",
        "2026-01-15,rent,30000,expense",
        "2026-02-03,food,2500,expense",
        "2026-02-10,transport,700,expense",
        "bad line",
        "2026-02-11,food,abc,expense",
        "",
        "2026-02-30,bonus,5000,income",
    ]
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")


def run_small_test():
    write_small_file("small_6.csv")
    result = analyze_finances("small_6.csv")
    print("Проверка на маленьком файле")
    print_result(result)
    ok = (
        result["income"] == 100000
        and result["expense"] == 34700
        and result["difference"] == 65300
        and result["top_category"] == "rent"
        and result["biggest_expense"] == ("2026-01-15", "rent", 30000.0)
        and result["top_month"] == "2026-01"
    )
    print("Результат верный:", ok)
    print()


def run_empty_test():
    with open("empty_6.csv", "w", encoding="utf-8") as file:
        file.write("")
    print("Проверка на пустом файле")
    print_result(analyze_finances("empty_6.csv"))
    print()


run_small_test()
run_empty_test()
generate_file("operations_6.csv", 5000)
print("Проверка на большом файле")
print_result(analyze_finances("operations_6.csv"))