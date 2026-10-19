from pathlib import Path


def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8")

    except FileNotFoundError:
        print("Файл не найден")

    except PermissionError:
        print("Нет прав на чтение файла")

    except IsADirectoryError:
        print("Указан каталог, а не файл")

    except UnicodeDecodeError:
        print("Не удалось прочитать текст в UTF-8")

    except OSError as error:
        print("Ошибка операционной системы:", error)

    return None


content = read_file(input("Путь к файлу: "))

if content is not None:
    print(content)