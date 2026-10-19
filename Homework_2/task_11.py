import re

with open("logs.txt", "r", encoding="utf-8") as file:
    text = file.read()

all_users = re.findall(r"\bUser (\d+)", text)

error_lines = [
    line for line in text.splitlines()
    if re.search(r"\bERROR\b", line)
]

error_users = re.findall(r"\bERROR User (\d+)", text)

print("Все ID пользователей:", sorted(set(all_users), key=int))

print("Строки с ошибками:")
for line in error_lines:
    print(line)

print("ID пользователей с ошибками:", sorted(set(error_users), key=int))