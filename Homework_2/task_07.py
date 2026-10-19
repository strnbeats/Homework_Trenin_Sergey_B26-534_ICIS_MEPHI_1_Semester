from pathlib import Path

directory = Path(input("Каталог: "))
extension = input("Расширение файла: ")

if not extension.startswith("."):
    extension = "." + extension

try:
    if not directory.is_dir():
        raise NotADirectoryError

    for path in directory.rglob("*"):
        if path.is_file() and path.suffix == extension:
            print(path, "-", path.stat().st_size, "байт")

except OSError as error:
    print("Ошибка:", error)