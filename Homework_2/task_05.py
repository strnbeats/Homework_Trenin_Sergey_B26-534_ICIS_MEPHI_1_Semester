import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    student["passed"] = student["score"] >= 60

if students:
    best = max(students, key=lambda student: student["score"])
    print("Лучший студент:", best["name"])
    print("Балл:", best["score"])

with open("students_updated.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print("Данные сохранены")