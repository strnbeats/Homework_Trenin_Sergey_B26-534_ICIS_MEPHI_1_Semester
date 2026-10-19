from pathlib import Path

path = Path("text.txt")

lines_count = 0
words_count = 0
chars_count = 0
longest_line = 0

with path.open("r", encoding="utf-8") as file:
    for line in file:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line)
        longest_line = max(longest_line, len(line.rstrip("\n")))

print("Количество строк:", lines_count)
print("Количество слов:", words_count)
print("Количество символов:", chars_count)
print("Длина самой длинной строки:", longest_line)