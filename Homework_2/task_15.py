from io import StringIO


def count_lines(stream):
    return sum(1 for line in stream)


with open("data.txt", "r", encoding="utf-8") as file:
    print("Строк в файле:", count_lines(file))


text = StringIO("first\nsecond\nthird")
print("Строк в StringIO:", count_lines(text))