from pathlib import Path

directory = Path(input("Введите путь к каталогу: "))

if not directory.is_dir():
    print("Каталог не существует")
else:
    files = [p for p in directory.iterdir() if p.is_file()]
    folders = [p for p in directory.iterdir() if p.is_dir()]
    python_files = list(directory.glob("*.py"))

    total_size = sum(p.stat().st_size for p in files)

    print("Количество файлов:", len(files))
    print("Количество подкаталогов:", len(folders))
    print("Python-файлы:")

    for path in python_files:
        print(path)

    print("Общий размер файлов:", total_size, "байт")