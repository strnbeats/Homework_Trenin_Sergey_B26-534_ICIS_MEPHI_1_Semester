import re
from collections import Counter

counts = Counter()
error_users = set()

with open("logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        match = re.search(r"\b(INFO|WARNING|ERROR)\b", line)

        if match:
            counts[match.group(1)] += 1

        if "ERROR" in line:
            user = re.search(r"\bUser (\d+)", line)

            if user:
                error_users.add(user.group(1))

print("INFO:", counts["INFO"])
print("WARNING:", counts["WARNING"])
print("ERROR:", counts["ERROR"])
print("Пользователи с ошибками:", sorted(error_users, key=int))