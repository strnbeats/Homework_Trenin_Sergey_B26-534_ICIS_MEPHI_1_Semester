import re

text = input("Введите текст: ")

pattern = (
    r"(?<!\w)(?:\+7|8)\s*"
    r"(?:\(\d{3}\)|\d{3})\s+"
    r"\d{3}-\d{2}-\d{2}(?!\w)"
)

phones = re.findall(pattern, text)

for phone in phones:
    print(phone)