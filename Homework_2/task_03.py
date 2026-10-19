import csv
from collections import defaultdict

with open("students.csv", "r", encoding="utf-8", newline="") as file:
    students = list(csv.DictReader(file))

scores = [int(student["score"]) for student in students]

if students:
    print("Средний балл:", sum(scores) / len(scores))

    best = max(students, key=lambda student: int(student["score"]))
    print("Лучший студент:", best["name"])
    print("Его балл:", best["score"])

    groups = defaultdict(list)

    for student in students:
        groups[student["group"]].append(int(student["score"]))

    for group, group_scores in sorted(groups.items()):
        print(
            f"Средний балл группы {group}: "
            f"{sum(group_scores) / len(group_scores):.2f}"
        )