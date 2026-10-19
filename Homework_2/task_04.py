import csv

with open("products.csv", "r", encoding="utf-8", newline="") as source:
    reader = csv.DictReader(source)
    fieldnames = reader.fieldnames
    products = [
        row for row in reader
        if float(row["price"]) > 100
    ]

with open("expensive.csv", "w", encoding="utf-8", newline="") as destination:
    writer = csv.DictWriter(destination, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("Файл expensive.csv создан")